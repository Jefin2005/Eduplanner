from collections import defaultdict
from django.shortcuts import render
from .models import TimetableEntry
def dashboard(request):
    return render(request, "dashboard.html")
def generate_timetable(request):
    entries = TimetableEntry.objects.all()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Slots only for DISPLAY
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

    # Store only teaching periods (1–7)
    timetable = defaultdict(dict)
    for entry in entries:
        timetable[entry.day][entry.period] = entry.subject.name

    context = {
        "days": days,
        "time_slots": time_slots,
        "timetable": timetable,
    }

    return render(request, "timetable.html", context)
