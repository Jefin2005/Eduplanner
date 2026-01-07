from django.shortcuts import render
from collections import defaultdict

from academics.models import Department, Semester, ClassRoomGroup, Subject, Faculty
from .models import TimetableEntry


# =========================
# DASHBOARD VIEW
# =========================
def dashboard(request):
    """
    Simple dashboard page with a Generate Timetable button
    """
    return render(request, "dashboard.html")


# =========================
# GENERATE TIMETABLE VIEW
# =========================
def generate_timetable(request):
    # Clear old timetable
    TimetableEntry.objects.all().delete()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods_per_day = 7

    # ✅ SELECT DEPARTMENT + SEMESTER (IMPORTANT)
    department = Department.objects.get(name="CS")
    semester = Semester.objects.get(department=department, number=5)

    class_groups = ClassRoomGroup.objects.filter(semester=semester)
    subjects = list(Subject.objects.filter(semester=semester))
    faculties = list(Faculty.objects.filter(department=department))

    for class_group in class_groups:
        for day in days:
            for period in range(1, periods_per_day + 1):
                subject = subjects[(period - 1) % len(subjects)]
                faculty = faculties[(period - 1) % len(faculties)]

                TimetableEntry.objects.create(
                    day=day,
                    period=period,
                    class_group=class_group,
                    subject=subject,
                    faculty=faculty,
                    classroom=None  # can be assigned later
                )

    timetable_by_class = defaultdict(list)
    for entry in TimetableEntry.objects.all():
        timetable_by_class[entry.class_group].append(entry)

    return render(
        request,
        "timetable.html",
        {"timetable_by_class": timetable_by_class}
    ) 