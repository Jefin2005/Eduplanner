from django.contrib import admin
from django.urls import path
from scheduling.views import dashboard, generate_timetable

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("generate/", generate_timetable, name="generate"),
    path("admin/", admin.site.urls),
]
