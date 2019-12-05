from django.urls import path
from .views import * #ProjectListView,ProjectCreateView, ProjectDetailView

urlpatterns = [
               path(
                   "workbook/",
                   ProjectListView.as_view(),
                   name="project-list-view",
               ),
               path(
               		"workbook/add/",
               		ProjectCreateView.as_view(),
               		name='project-create-view',
               	),
               path(
               		"workbook/detail/",
               		ProjectCreateView.as_view(),
               		name='project-detail-view',
               	),
               path(
               		"workbook/delete/",
               		ProjectCreateView.as_view(),
               		name='project-delete-view',
               	),
               path(
               		"workbook/update/",
               		ProjectUpdateView.as_view(),
               		name='project-update-view',
               	),
               path(
               		"task/",
               		TaskListView.as_view(),
               		name='task-list-view',
               	),
               path(
               		"task/detail/",
               		TaskDetailView.as_view(),
               		name='task-detail-view',
               	),
               path(
               		"task/update/",
               		TaskUpdateView.as_view(),
               		name='task-update-view',
               	),
               path(
               		"task/delete/",
               		TaskDeleteView.as_view(),
               		name='task-delete-view',
               	),

]