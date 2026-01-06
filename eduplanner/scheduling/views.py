from django.shortcuts import render, redirect
from collections import defaultdict

# Timetable model
from .models import TimetableEntry

# Dashboard forms
from academics.forms import (
    CollegeForm,
    DepartmentForm,
    SemesterForm,
    ClassRoomGroupForm,
    FacultyForm,
    SubjectForm,
)

# =========================
# DASHBOARD VIEW (ADMIN INPUT)
# =========================
def dashboard(request):
    context = {
        "college_form": CollegeForm(),
        "department_form": DepartmentForm(),
        "semester_form": SemesterForm(),
        "class_form": ClassRoomGroupForm(),
        "faculty_form": FacultyForm(),
        "subject_form": SubjectForm(),
    }

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "college":
            CollegeForm(request.POST).save()

        elif form_type == "department":
            DepartmentForm(request.POST).save()

        elif form_type == "semester":
            SemesterForm(request.POST).save()

        elif form_type == "class":
            ClassRoomGroupForm(request.POST).save()

        elif form_type == "faculty":
            FacultyForm(request.POST).save()

        elif form_type == "subject":
            SubjectForm(request.POST).save()

        return redirect("/")

    return render(request, "dashboard.html", context)


# =========================
# GENERATE TIMETABLE VIEW
# =========================
def generate_timetable(request):
    entries = TimetableEntry.objects.all()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # DISPLAY SLOTS (includes RECESS & LUNCH)
    time_slots = [
        "8:45-9:35",
        "9:35-10:25",
        "RECESS",
        "10:35-11:30",
        "11:30-12:15",
        "LUNCH",
        "1:05-1:55",
        "RECESS",
        "2:05-2:55",
        "2:55-3:45",
    ]

    # timetable[day][period] = subject
    timetable = defaultdict(dict)

    for entry in entries:
        timetable[entry.day][entry.period] = entry.subject.name

    context = {
        "days": days,
        "time_slots": time_slots,
        "timetable": timetable,
    }

    return render(request, "timetable.html", context)
