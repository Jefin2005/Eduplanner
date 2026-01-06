from django import forms
from .models import College, Department, Semester, ClassRoomGroup, Faculty, Subject

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['college', 'name']


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['department', 'number']


class ClassRoomGroupForm(forms.ModelForm):
    class Meta:
        model = ClassRoomGroup
        fields = ['semester', 'section_name']


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'department', 'max_hours']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'weekly_hours', 'semester', 'faculty']
