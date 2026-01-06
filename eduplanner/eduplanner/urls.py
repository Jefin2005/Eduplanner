from django.contrib import admin
from django.urls import path
from scheduling.views import dashboard, generate_timetable

urlpatterns = [
    path("", dashboard),
    path("generate/", generate_timetable),
    path("admin/", admin.site.urls),
]
