from django import forms
from dork.models import Project, Task, SubTask

class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class SubTaskCreateForm(forms.ModelForm):

    class Meta:
        model = SubTask
        fields = '__all__'
