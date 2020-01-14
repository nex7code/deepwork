from django.urls import path
from dork.api.views import (
							ProjectListApi,
							ProjectDetailApi,
							ProjectUpdateApi,
							ProjectDeleteApi,
							ProjectCreateApi
						)


app_name = 'dork'

urlpatterns = [
               path(
	               "workboard/",
	               ProjectListApi.as_view(),
	               name="project-list-api-view",
               ),
               path(
               		"workboard/detail/<int:pk>/",
               		ProjectDetailApi.as_view(),
               		name='project-detail-api-view',
               	),
               path(
               		"workboard/delete/<int:pk>/",
               		ProjectDeleteApi.as_view(),
               		name='project-delete-api-view',
               	),
               path(
               		"workboard/update/<int:pk>/",
               		ProjectUpdateApi.as_view(),
               		name='project-update-api-view',
               	),
               path(
               		"workboard/add/",
               		ProjectCreateApi.as_view(),
               		name='project-create-api-view',
               	),
           ]