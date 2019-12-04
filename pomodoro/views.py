from django.shortcuts import render, render_to_response
from django.views import generic
from .models import Pomodoro

class PomodoroTemplateView(generic.TemplateView):
    model = Pomodoro
    template_name = 'pomodoro/pomodoro_template_view.html'

