from django.contrib import admin
from django.urls import path
from scheduling.views import generate_timetable, dashboard

urlpatterns = [
    path('', dashboard),
    path('generate/', generate_timetable),
    path('admin/', admin.site.urls),
]
