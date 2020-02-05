from django import forms
from dork.models import WorkBoard, Task, SubTask


class WorkBoardCreateForm(forms.ModelForm):
    class Meta:
        model = WorkBoard
        fields = "__all__"


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class SubTaskCreateForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = "__all__"
