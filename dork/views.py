from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from django.views import generic
from dork.models import Project, Task, SubTask
from dork.forms import ProjectCreateForm, TaskCreateForm, SubTaskCreateForm



class ProjectListView(generic.ListView):
	model = Project
	template_name = 'dork/project/project_list_view.html'


class ProjectCreateView(generic.edit.CreateView):
	model = Project
	# fields = '__all__'
	form_class = ProjectCreateForm
	template_name = 'dork/project/project_create_view.html'
	success_url = reverse_lazy('project-list-view')


class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = 'dork/project/project_detail_view.html'


class ProjectUpdateView(generic.edit.UpdateView):
	model = Project
	# fields = '__all__'#('title',)
	form_class = ProjectCreateForm
	template_name = 'dork/project/project_update_view.html'
	success_url = reverse_lazy('project-list-view')


class ProjectDeleteView(generic.edit.DeleteView):
	model = Project
	form_class = ProjectCreateForm
	template_name = 'dork/project/project_delete_view.html'
	success_url = reverse_lazy('project-list-view')


# Task Views

class TaskListView(generic.ListView):
	model = Task
	template_name = 'dork/task/task_list_view.html'


class TaskCreateView(generic.edit.CreateView):
	model = Task
	form_class = TaskCreateForm
	template_name = 'dork/task/task_create_view.html'
	success_url = reverse_lazy('task-list-view')


class TaskDetailView(generic.DetailView):
	model = Task
	template_name = 'dork/task/task_detail_view.html'


class TaskUpdateView(generic.edit.UpdateView):
	model = Task
	form_class = TaskCreateForm
	template_name = 'dork/task/task_update_view.html'
	success_url = reverse_lazy('task-list-view')


class TaskDeleteView(generic.edit.DeleteView):
	model = Task
	template_name = 'dork/task/task_delete_view.html'
	success_url = reverse_lazy('task-list-view')