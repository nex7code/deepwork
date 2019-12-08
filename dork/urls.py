from django.urls import path
from .views import * #ProjectListView,ProjectCreateView, ProjectDetailView

urlpatterns = [
               path(
                   "workboard/",
                   ProjectListView.as_view(),
                   name="project-list-view",
               ),
               path(
               		"workboard/add/",
               		ProjectCreateView.as_view(),
               		name='project-create-view',
               	),
               path(
               		"workboard/detail/",
               		ProjectCreateView.as_view(),
               		name='project-detail-view',
               	),
               path(
               		"workboard/delete/<int:pk>/",
               		ProjectDeleteView.as_view(),
               		name='project-delete-view',
               	),
               path(
               		"workboard/update/<int:pk>/",
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
               		"task/add/",
               		TaskCreateView.as_view(),
               		name='task-create-view',
               	),
               path(
               		"task/update/<int:pk>/",
               		TaskUpdateView.as_view(),
               		name='task-update-view',
               	),
               path(
               		"task/delete/<int:pk>/",
               		TaskDeleteView.as_view(),
               		name='task-delete-view',
               	),

]