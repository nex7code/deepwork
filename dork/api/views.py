from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from dork.models import Project
from dork.api.serializers import ProjectSerializer


class ProjectListApi(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailApi(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateApi(generics.UpdateAPIView):
	lookup_field = 'pk'
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class ProjectDeleteApi(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateApi(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer