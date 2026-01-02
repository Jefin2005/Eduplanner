import random
from django.shortcuts import render
from academics.models import Faculty, Subject, Classroom
from .models import TimetableEntry

def generate_timetable(request):
    TimetableEntry.objects.all().delete()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    faculties = list(Faculty.objects.all())
    subjects = list(Subject.objects.all())
    rooms = list(Classroom.objects.all())

    for day in days:
        for period in range(1, 5):
            TimetableEntry.objects.create(
                day=day,
                period=period,
                subject=random.choice(subjects),
                faculty=random.choice(faculties),
                classroom=random.choice(rooms),
            )

    return render(request, "timetable.html", {
        "entries": TimetableEntry.objects.all()
    })
