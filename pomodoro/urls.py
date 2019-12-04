from django.urls import path
from .views import PomodoroTemplateView

urlpatterns = [
               path(
                   "",
                   PomodoroTemplateView.as_view(),
                   name="tepmplate-view",
               ),
]