# academics/utils.py
from .models import College, Department, Semester, ClassRoomGroup

def setup_initial_data():
    college, _ = College.objects.get_or_create(
        name="SCMS School of Engineering & Technology"
    )

    department_names = ["CS", "EC", "EEE", "VLSI", "MCA", "DS", "CO"]

    for dept_name in department_names:
        dept, _ = Department.objects.get_or_create(
            college=college,
            name=dept_name
        )

        for sem_no in range(1, 9):
            semester, _ = Semester.objects.get_or_create(
                department=dept,
                number=sem_no
            )

            for section in ["A", "B", "C", "D"]:
                ClassRoomGroup.objects.get_or_create(
                    semester=semester,
                    section_name=section
                )
