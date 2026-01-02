from django.contrib import admin
from django.urls import path
from scheduling.views import generate_timetable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', generate_timetable),
]
