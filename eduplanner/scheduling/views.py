import random
from django.shortcuts import render
from academics.models import Faculty, Subject, Classroom
from .models import TimetableEntry

def generate_timetable(request):
    TimetableEntry.objects.all().delete()

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods_per_day = 4

    faculties = list(Faculty.objects.all())
    subjects = list(Subject.objects.all())
    rooms = list(Classroom.objects.all())

    # Tracking
    faculty_time = set()              # (faculty_id, day, period)
    room_time = set()                 # (room_id, day, period)
    faculty_day_load = {}             # (faculty_id, day) → count
    faculty_week_load = {}            # faculty_id → total hours

    for day in days:
        for period in range(1, periods_per_day + 1):

            attempts = 0
            while attempts < 30:
                subject = random.choice(subjects)
                faculty = random.choice(faculties)
                room = random.choice(rooms)

                f_key = (faculty.id, day, period)
                r_key = (room.id, day, period)
                fd_key = (faculty.id, day)

                # Rule‑1: Faculty clash
                if f_key in faculty_time:
                    attempts += 1
                    continue

                # Rule‑2: Room clash
                if r_key in room_time:
                    attempts += 1
                    continue

                # Rule‑3: Max 2 periods/day per faculty
                if faculty_day_load.get(fd_key, 0) >= 2:
                    attempts += 1
                    continue

                # Rule‑4: Weekly workload limit
                current_load = faculty_week_load.get(faculty.id, 0)
                if current_load + subject.weekly_hours > faculty.max_hours:
                    attempts += 1
                    continue

                # ✅ All rules satisfied → assign
                TimetableEntry.objects.create(
                    day=day,
                    period=period,
                    subject=subject,
                    faculty=faculty,
                    classroom=room
                )

                faculty_time.add(f_key)
                room_time.add(r_key)
                faculty_day_load[fd_key] = faculty_day_load.get(fd_key, 0) + 1
                faculty_week_load[faculty.id] = current_load + subject.weekly_hours

                break

    return render(request, "timetable.html", {
        "entries": TimetableEntry.objects.all()
    })
