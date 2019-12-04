#!/bin/bash
if rpm -q guestfs-tools libvirt qemu >> /dev/null; then
   echo "All required packages are installed"
else
   echo "All required packages: guestfs-tools, libvirt and qemu not installed, please install it and try again\n"
   exit 1
fi

##### Functions #######
function virt_v2v_copy(){
    if [[ -n "$PASSFILE" ]]; then
       virt-v2v-copy-to-local --password-file $PASSFILE -ic esx://root@$1?no_verify=1 $HOSTN
    else
       virt-v2v-copy-to-local -ic esx://root@$1?no_verify=1 $HOSTN
    fi
}

function ubuntu_customize() {
    cp $DIRNAME/vm_ubuntu.sh $TMPFILE
    sed -i "/bash/a HWADDR=$2\n" $TMPFILE
    virt-customize -d $1 --run "$TMPFILE" 1>> $LOGFILE 2>&1
}

function ubuntu16_customize() {
    cp $DIRNAME/vm_ubuntu16.sh $TMPFILE
    sed -i "/bash/a HWADDR=$2\n" $TMPFILE
    virt-customize -d $1 --run "$TMPFILE" 1>> $LOGFILE 2>&1
}

function sles_customize(){
    cp $DIRNAME/vm_sles.sh $TMPFILE
    virt-customize -d $1 --run "$TMPFILE" 1>> $LOGFILE 2>&1
}

function sles10_customize(){
    cp $DIRNAME/vm_sles10.sh $TMPFILE
    virt-customize -d $1 --run "$TMPFILE" 1>> $LOGFILE 2>&1
}

netmask2cidr(){
  case $1 in
      0x*)
      local hex=${1#0x*} quad=
      while [ -n "${hex}" ]; do
        local lastbut2=${hex#??*}
        quad=${quad}${quad:+.}0x${hex%${lastbut2}*}
        hex=${lastbut2}
      done
      set -- ${quad}
      ;;
  esac

  local i= len=
  local IFS=.
  for i in $1; do
    while [ ${i} != "0" ]; do
      len=$((${len} + ${i} % 2))
      i=$((${i} >> 1))
    done
  done

  echo "${len}"
}

function subnet_change() {
  NETMASK=$(ifconfig br0 | grep "inet addr" | awk '{ print $4 }' | awk -F':' '{ print $2 }')
  MASK=$(netmask2cidr $NETMASK)
  GATEWAY=$(ip route | grep default | awk '{ print $3 }')
  BROADCAST=$(ifconfig br0 | grep "inet addr" | awk '{ print $3 }' | awk -F':' '{ print $2 }')
  NETWORK=$(ip route | grep link | awk -F'/' '{ print $1 }')
  NET=$(echo $NETWORK | cut -d'.' -f1,2,3)
  if [[ $2 =~ $NET ]]; then
     $DIRNAME/subnet-change.sh -p $1 -i $2 -s $MASK -g $GATEWAY -b $BROADCAST -w $NETWORK -m $HOSTN
  else
     echo "Please use IP in same subnet of kvm host" 
  fi
}


function img_cc() {
  if ls -la $BASEDIR/$HOSTN/$HOSTN-disk* 1>> $LOGFILE 2>&1; then
     if ls $BASEDIR/$HOSTN/$HOSTN.xml; then
        NETCOUNT=$(grep "mac address" $BASEDIR/$HOSTN/$HOSTN.xml | wc -l)
        if [[ $NETCOUNT -gt 1 ]]; then
           echo "XML file is showing $NETCOUNT network devices for vm, vm will be up with first network interface.. please check and configure second network if required"
        fi
        HWADDR=$(grep -m1 "mac address" $BASEDIR/$HOSTN/$HOSTN.xml | awk -F'"' '{ print $2 }')
        VCPU=$(grep vcpu $BASEDIR/$HOSTN/$HOSTN.xml | grep -o '[[:digit:]]*')
        MEMORY=$(grep memory $BASEDIR/$HOSTN/$HOSTN.xml | grep -o '[[:digit:]]*')
        MEM=$(( $MEMORY / 1024 ))
     else
        echo "$HOSTN xml file is not found, CPU & mem details would be fetched from nodes database"
        HWADDR=$(umatch nodes $HOSTN macaddr)
        VCPU=$(umatch nodes $HOSTN cpunum)
        MEM=$(umatch nodes $HOSTN memory)
     fi
     n=1
     VMDK=($(ls $BASEDIR/$HOSTN/$HOSTN-disk* ))
     DISKS=()
     SLES10DISK=()
     echo "VMDK to QCOW2 convertion is in progress"
     for i in ${VMDK[@]}
     do
       qemu-img convert -O qcow2 $i "$BASEDIR/$HOSTN-disk$n.qcow2" 1>> $LOGFILE 2>&1
       DISKS+=("--disk $BASEDIR/$HOSTN-disk$n.qcow2,bus=virtio")
       SLES10DISK+=("--disk $BASEDIR/$HOSTN-disk$n.qcow2")
       n=$(( $n + 1 ))
     done 
     OSFILE=$(mktemp /tmp/OS.XXXXXX)
     if ls $BASEDIR/$HOSTN-disk*.qcow2 1>> $LOGFILE 2>&1; then
        echo "Disks converstion has successfully completed"
        echo "Defining host domain"
        virt-inspector -a $BASEDIR/$HOSTN-disk1.qcow2 | virt-inspector --xpath '//distro|//product_name|//major_version' 2>&1 >> $OSFILE 
        if egrep -i 'major_version>10' $OSFILE 1>> $LOGFILE 2>&1; then
           virt-install --connect qemu:///system -n $HOSTN -r $MEM --vcpus=$VCPU ${SLES10DISK[@]} --virt-type kvm --machine pc --vnc --os-type linux --import --network=bridge:br0,mac=$HWADDR --boot hd,network,menu=on --dry-run --print-xml > /tmp/$HOSTN.xml
        else
           virt-install --connect qemu:///system -n $HOSTN -r $MEM --vcpus=$VCPU ${DISKS[@]} --virt-type kvm --machine pc --vnc --os-type linux --import --network=bridge:br0,model=virtio,mac=$HWADDR --boot hd,network,menu=on --dry-run --print-xml > /tmp/$HOSTN.xml
        fi
        virsh define /tmp/$HOSTN.xml 1>> $LOGFILE 2>&1
        if grep -i ubuntu $OSFILE 1>> $LOGFILE 2>&1; then
           if egrep -i 'major_version>16' $OSFILE 1>> $LOGFILE 2>&1; then
              ubuntu16_customize $HOSTN $HWADDR
           else
              ubuntu_customize $HOSTN $HWADDR
           fi
           echo "Hard coded ubuntu network device config and disabled vmware tools"
        elif egrep -i 'sles' $OSFILE 1>> $LOGFILE 2>&1; then
           if egrep -i 'major_version>11|major_version>12' $OSFILE 1>> $LOGFILE 2>&1; then
              sles_customize $HOSTN
              echo "Disabled vmware tools in sles"
           elif egrep -i 'major_version>10' $OSFILE 1>> $LOGFILE 2>&1; then
              sles10_customize $HOSTN
           fi
        fi
        if [[ "$CHANGEIP" == "yes" ]]; then
           echo "Please register DDI entry with new IP\n"
           if [[ -n $OLDIP ]] && [[ -n $NEWIP ]]; then
              subnet_change $OLDIP $NEWIP
           else
              read -p "Please enter oldip: " OLDIP
              read -p "Please enter newip: " NEWIP
              subnet_change $OLDIP $NEWIP
           fi
        else
           echo "Starting up vm using command: 'virsh start $HOSTN'"
           virsh start $HOSTN
        fi
     else
       echo "qcow2 convertion failed, please check $LOGFILE for details"
     fi
     rm $TMPFILE
     rm $OSFILE
     rm -rf $BASEDIR/$HOSTN
  else
     echo "Disk is not copied from esxi server to KVM host, please check the logs for detail"
  fi
}


########### Main Code ###############
if [[ $1 == '--help' ]] ; then
  echo "Usage with subnet change: $0 --hostname <GUESTNAME>  --changeip --oldip <OLDIP> --newip <NEWIP>"
  echo "Usage without subnet change: $0 --hostname <GUESTNAME>"
  echo "You may also give --esxi option if esxi hostname is not updated node database: $0 --hostname <GUESTNAME> --esxi <ESXI-SERVER-NAME>"
  echo "Usage Example: $0 --hostname musxtestvm006 --changeip --oldip 10.216.40.42 -newip 10.216.137.78"
  exit 0
fi

NOW=$(date +"%Y%m%d"_"%T")
LOGFILE="/tmp/$NOW-$HOSTN-img_convert.log"
POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -h|--hostname)
    HOSTN="$2"
    shift 
    shift 
    ;;
    -e|--esxi)
    ESXIHOST="$2"
    shift
    shift
    ;;
    -e|--passfile)
    PASSFILE="$2"
    shift
    shift
    ;;
    -c|--changeip)
    CHANGEIP="yes"
    shift 
    ;;
    -|--oldip)
    OLDIP="$2"
    shift 
    shift 
    ;;
    --newip)
    NEWIP="$2"
    shift
    shift
    ;;
    *)    
    POSITIONAL+=("$1") 
    shift 
    ;;
esac
done
CWD=`pwd`
BASEDIR="/var/lib/libvirt/images"
TMPFILE=$(mktemp /tmp/img-convert.XXXXXX)
DIRNAME=$( dirname $0 )
if [[ -n "$HOSTN" ]]; then
   LOGFILE="/tmp/$NOW-$HOSTN-img_convert.log"
   if ls -la $BASEDIR/$HOSTN/$HOSTN-disk* 1>> $LOGFILE 2>&1; then 
      echo "vmdk files alredya exists, running qcow2 convertion"
      img_cc
   else
      mkdir $BASEDIR/$HOSTN
      cp passfile $BASEDIR/$HOSTN
      cd $BASEDIR/$HOSTN
      if [[ -n "$ESXIHOST" ]]; then
         virt_v2v_copy $ESXIHOST
      else
         ESXI=$(umatch nodes $HOSTN location | awk -F':' '{ print $2 }')
         virt_v2v_copy $ESXI
      fi
      cd $CWD
      img_cc
   fi
else
   echo "--hostname option cannot be blanked, please use --help option to check the usage" 
fi
