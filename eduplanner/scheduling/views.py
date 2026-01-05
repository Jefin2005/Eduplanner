TIME_SLOTS = [
    "8:45-9:35",
    "9:35-10:25",
    "10:35-11:30",
    "11:30-12:15",
    "1:05-1:55",
    "2:05-2:55",
    "2:55-3:45",
]

from django.shortcuts import render
from academics.models import Faculty, Subject, Classroom
from .models import TimetableEntry
from ga_engine.ga_runner import run_ga

def dashboard(request):
    return render(request, "dashboard.html")

from collections import defaultdict
from django.shortcuts import render
from .models import TimetableEntry

def generate_timetable(request):
    entries = TimetableEntry.objects.all()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    timetable = defaultdict(dict)

    for entry in entries:
        timetable[entry.day][entry.period] = entry.subject.name

    context = {
        "days": days,
        "time_slots": [
            "8:45-9:35",
            "9:35-10:25",
            "10:35-11:30",
            "11:30-12:15",
            "1:05-1:55",
            "2:05-2:55",
            "2:55-3:45",
        ],
        "timetable": timetable,
    }

    return render(request, "timetable.html", context)

