from django.db import models
from academics.models import Subject, Faculty, Classroom, ClassRoomGroup


class TimetableEntry(models.Model):
    DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
    ]

    day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES
    )

    period = models.IntegerField()

    # 🔑 NEW: timetable is per CLASS (A / B / C / D)
    class_group = models.ForeignKey(
        ClassRoomGroup,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE
    )

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.class_group} | {self.day} | Period {self.period}"
