from django.contrib import admin
from .models import (
    College,
    Department,
    Semester,
    ClassRoomGroup,
    Faculty,
    Subject,
)

# ======================
# BASIC REGISTRATIONS
# ======================

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Semester)
admin.site.register(ClassRoomGroup)


# ======================
# FACULTY ADMIN (ID ONLY)
# ======================

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("faculty_id", "department", "max_hours")
    readonly_fields = ("faculty_id",)
    ordering = ("department", "faculty_id")


# ======================
# SUBJECT ADMIN
# ======================

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "semester", "faculty", "weekly_hours")
    list_filter = ("semester",)

