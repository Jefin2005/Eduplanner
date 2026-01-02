from django.db import models
from academics.models import Faculty, Subject, Classroom

class TimetableEntry(models.Model):
    day = models.CharField(max_length=10)
    period = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day} - {self.subject}"

