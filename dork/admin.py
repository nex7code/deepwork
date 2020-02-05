from django.contrib import admin

from .models import WorkBoard, Task, SubTask

admin.site.register(WorkBoard)
admin.site.register(Task)
admin.site.register(SubTask)

