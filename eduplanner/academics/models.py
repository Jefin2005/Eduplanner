from django.db import models

# ======================
# COLLEGE STRUCTURE
# ======================

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
        return f"{self.department.name} - S{self.number}"


class ClassRoomGroup(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=1)  # A, B, C, D

    def __str__(self):
        return f"{self.semester} - {self.section_name}"


# ======================
# FACULTY (WITH AUTO ID)
# ======================

from django.db import models

class Faculty(models.Model):
    faculty_id = models.CharField(
        max_length=10,
        unique=True,
        blank=True
    )
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE
    )
    max_hours = models.IntegerField()

    def save(self, *args, **kwargs):
        """
        Auto-generate Faculty ID like:
        SCS01, SCS02, SEC01, etc.
        """
        if not self.faculty_id:
            dept_code = self.department.name.upper()

            last_faculty = Faculty.objects.filter(
                department=self.department,
                faculty_id__startswith=f"S{dept_code}"
            ).order_by("faculty_id").last()

            if last_faculty:
                last_number = int(last_faculty.faculty_id[-2:])
                new_number = last_number + 1
            else:
                new_number = 1

            self.faculty_id = f"S{dept_code}{new_number:02d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.faculty_id

# ======================
# SUBJECTS
# ======================

class Subject(models.Model):
    name = models.CharField(max_length=100)
    weekly_hours = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


# ======================
# PHYSICAL CLASSROOMS
# ======================

class Classroom(models.Model):
    room_no = models.CharField(max_length=20)
    room_type = models.CharField(
        max_length=10,
        choices=[("THEORY", "Theory"), ("LAB", "Lab")]
    )

    def __str__(self):
        return self.room_no
