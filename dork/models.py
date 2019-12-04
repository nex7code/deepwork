from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=50)
	priority = models.IntegerField()
	color = models.CharField(max_length=100)
	backgroud_image = models.ImageField()
	create_date = models.DateTimeField(auto_now=True, null=False, blank=False)
	start_time = models.DateTimeField(auto_now=False, blank=True, null=True)
	expected_end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
	real_end_time =  models.DateTimeField(auto_now=False, blank=True, null=True)
	expected_total_time = models.IntegerField()
	real_total_time = models.IntegerField()
	description = models.TextField()

	class Meta(object):
	    verbose_name = ('WORKBOARD')
	    verbose_name_plural = ('WORKBOARD')
	    app_label = 'dork'

	def __str__(self):
	    return '%s - %s' % (self.title, self.priority)




class Task(models.Model):
	UNPLANNED = 'UN'
	SCHEDULED = 'SC'
	COMPLETED = 'CM'
	CANCELLED = 'CN'

	STATUS_CHOICES = [
			(UNPLANNED ,'Unplanned'),
			(SCHEDULED , 'Scheduled'),
			(COMPLETED , 'Completed'),
			(CANCELLED , 'Cancelled'),
		]

	title = models.CharField(max_length=50)
	priority = models.IntegerField()
	color = models.CharField(max_length=100)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	create_date = models.DateTimeField(auto_now=True, null=False, blank=False)
	start_time = models.DateTimeField(auto_now=False, blank=True, null=True)
	expected_end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
	real_end_time =  models.DateTimeField(auto_now=False, blank=True, null=True)
	expected_total_time = models.IntegerField()
	real_total_time = models.IntegerField()    
	description = models.TextField()
	status =  models.CharField(max_length=2,choices=STATUS_CHOICES, default=UNPLANNED)

	class Meta(object):
		verbose_name = ('TASK')
		verbose_name_plural = ('TASK')
		app_label = 'dork'

	def __str__(self):
		return '%s - %s' % (self.title, self.priority)

