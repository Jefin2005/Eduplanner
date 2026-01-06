from django.contrib import admin
from .models import College, Department, Semester, ClassRoomGroup, Faculty, Subject

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(ClassRoomGroup)
admin.site.register(Faculty)
admin.site.register(Subject)

