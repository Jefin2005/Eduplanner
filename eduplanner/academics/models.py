from django.db import models

class College(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Semester(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"Semester {self.number}"


class ClassRoomGroup(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=10)  # A, B, C

    def __str__(self):
        return f"{self.semester} - {self.section_name}"


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    max_hours = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=100)
    weekly_hours = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

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
