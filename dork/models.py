from django.db import models
from django.contrib.auth.models import User

# WorkBoard is basically the project
class WorkBoard(models.Model):
    owner = models.ForeignKey(
        User, related_name="workboards", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=50)
    priority = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    backgroud_image = models.ImageField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True, null=False, blank=False)
    start_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    expected_end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    real_end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    expected_total_time = models.IntegerField(blank=True, null=True)
    real_total_time = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name = "WORKBOARD"
        verbose_name_plural = "WORKBOARD"
        app_label = "dork"

    def __str__(self):
        return "%s - %s" % (self.title, self.priority)


class Task(models.Model):
    UNPLANNED = "UN"
    SCHEDULED = "SC"
    COMPLETED = "CM"
    CANCELLED = "CN"

    STATUS_CHOICES = [
        (UNPLANNED, "Unplanned"),
        (SCHEDULED, "Scheduled"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled"),
    ]

    title = models.CharField(max_length=50)
    priority = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    workboard = models.ForeignKey(
        WorkBoard, related_name="tasks", on_delete=models.CASCADE
    )
    create_date = models.DateTimeField(auto_now=True, null=False, blank=False)
    start_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    expected_end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    real_end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    expected_total_time = models.IntegerField(blank=True, null=True)
    real_total_time = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=UNPLANNED)

    class Meta(object):
        verbose_name = "TASK"
        verbose_name_plural = "TASK"
        app_label = "dork"

    def __str__(self):
        return "%s - %s" % (self.title, self.priority)


class SubTask(models.Model):
    title = models.CharField(max_length=50)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta(object):
        verbose_name = "SUBTASK"
        verbose_name_plural = "SUBTASKS"
        app_label = "dork"

    def __str__(self):
        return "%s - %s" % (self.title, self.status)

