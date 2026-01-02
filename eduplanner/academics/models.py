from django.db import models

class Faculty(models.Model):
    CATEGORY_CHOICES = [
        ("PROFESSOR", "Professor"),
        ("ASSOCIATE", "Associate Professor"),
        ("ASSISTANT", "Assistant Professor"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    max_hours = models.IntegerField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    SUBJECT_TYPE = [
        ("THEORY", "Theory"),
        ("LAB", "Lab"),
    ]

    name = models.CharField(max_length=100)
    subject_type = models.CharField(max_length=10, choices=SUBJECT_TYPE)
    weekly_hours = models.IntegerField()

    def __str__(self):
        return self.name


class Classroom(models.Model):
    room_no = models.CharField(max_length=20)
    room_type = models.CharField(
        max_length=10,
        choices=[("THEORY", "Theory"), ("LAB", "Lab")]
    )

    def __str__(self):
        return self.room_no
