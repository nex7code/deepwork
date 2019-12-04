from django.db import models

# Create your models here.

class Pomodoro(models.Model):
    task = models.CharField(max_length=100, blank=False, null=False)
    length = models.IntegerField(blank=False, help_text="time in minutes")
    description = models.TextField(blank=False,null=False) 
        

    class Meta(object):
        verbose_name = ('pomodoro')
        verbose_name_plural = ('pomodoros')
        app_label = 'pomodoro'

    def __str__(self):
        return '%s - %s' % (self.task, self.length)
        