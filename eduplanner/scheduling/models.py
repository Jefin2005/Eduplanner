from django.db import models
from academics.models import Department, Subject, Faculty, Classroom


class TimetableEntry(models.Model):
    day = models.CharField(max_length=10)
    period = models.IntegerField()

    department = models.ForeignKey(
        Department,
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
        return f"{self.day} - Period {self.period}"
