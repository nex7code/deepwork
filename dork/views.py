from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from django.views import generic
from dork.models import WorkBoard, Task, SubTask
from dork.forms import WorkBoardCreateForm, TaskCreateForm, SubTaskCreateForm

# WorkBoard is basically the project


class WorkBoardListView(generic.ListView):
    model = WorkBoard
    template_name = "dork/project/project_list_view.html"


class WorkBoardCreateView(generic.edit.CreateView):
    model = WorkBoard
    # fields = '__all__'
    form_class = WorkBoardCreateForm
    template_name = "dork/project/project_create_view.html"
    success_url = reverse_lazy("project-list-view")


class WorkBoardDetailView(generic.DetailView):
    model = WorkBoard
    template_name = "dork/project/project_detail_view.html"


class WorkBoardUpdateView(generic.edit.UpdateView):
    model = WorkBoard
    # fields = '__all__'#('title',)
    form_class = WorkBoardCreateForm
    template_name = "dork/project/project_update_view.html"
    success_url = reverse_lazy("project-list-view")


class WorkBoardDeleteView(generic.edit.DeleteView):
    model = WorkBoard
    form_class = WorkBoardCreateForm
    template_name = "dork/project/project_delete_view.html"
    success_url = reverse_lazy("project-list-view")


# Task Views


class TaskListView(generic.ListView):
    model = Task
    template_name = "dork/task/task_list_view.html"


class TaskCreateView(generic.edit.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "dork/task/task_create_view.html"
    success_url = reverse_lazy("task-list-view")


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "dork/task/task_detail_view.html"


class TaskUpdateView(generic.edit.UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "dork/task/task_update_view.html"
    success_url = reverse_lazy("task-list-view")


class TaskDeleteView(generic.edit.DeleteView):
    model = Task
    template_name = "dork/task/task_delete_view.html"
    success_url = reverse_lazy("task-list-view")

