from django.shortcuts import render
from academics.models import Faculty, Subject, Classroom
from .models import TimetableEntry
from ga_engine.ga_runner import run_ga

def generate_timetable(request):
    TimetableEntry.objects.all().delete()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods_per_day = 4

    subjects = list(Subject.objects.all())
    faculties = list(Faculty.objects.all())
    rooms = list(Classroom.objects.all())

    best_timetable = run_ga(
        days=days,
        periods=periods_per_day,
        subjects=subjects,
        faculties=faculties,
        rooms=rooms
    )

    for entry in best_timetable.entries:
        TimetableEntry.objects.create(
            day=entry["day"],
            period=entry["period"],
            subject=entry["subject"],
            faculty=entry["faculty"],
            classroom=entry["room"]
        )

    return render(request, "timetable.html", {
        "entries": TimetableEntry.objects.all()
    })
