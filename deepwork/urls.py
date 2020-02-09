from django.contrib import admin
from django.urls import path, include
import pomodoro.urls
import dork.urls
import frontend.urls
import accounts.urls
 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("pomodoro/", include(pomodoro.urls)),
    path("dork/", include(dork.urls)),
    path("", include(accounts.urls)),
    path("", include(frontend.urls)),
    path("", include(dork.urls)),
]
