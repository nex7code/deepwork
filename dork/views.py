from django.shortcuts import render, render_to_response
from django.views import generic
from .models import Project, Task, SubTask


class ProjectListView(generic.ListView):
	model = Project
	template_name = 'dork/project_list_view.html'


class ProjectCreateView(generic.edit.CreateView):
	model = Project
	fields = '__all__'
	template_name = 'dork/project_create_view.html'


class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = 'dork/project_detail_view.html'


class ProjectUpdateView(generic.edit.UpdateView):
	model = Project
	template_name = 'dork/project_create_view.html'


class ProjectDeleteView(generic.edit.DeleteView):
	model = Project
	template_name = 'dork/project_detail_view.html'


# Task Views

class TaskListView(generic.ListView):
	model = Task
	template_name = 'dork/task_list_view.html'


class TaskCreateView(generic.edit.CreateView):
	model = Task
	fields = '__all__'
	template_name = 'dork/task_create_view.html'


class TaskDetailView(generic.DetailView):
	model = Task
	template_name = 'dork/task_detail_view.html'


class TaskUpdateView(generic.edit.UpdateView):
	model = Task
	template_name = 'dork/task_create_view.html'


class TaskDeleteView(generic.edit.DeleteView):
	model = Task
	template_name = 'dork/task_detail_view.html'