from .models import College, Department, Semester, ClassRoomGroup

def setup_initial_data():
    college, _ = College.objects.get_or_create(
        name="SCMS School of Engineering & Technology"
    )

    departments = ["CS", "EC", "EEE", "VLSI", "MCA", "DS", "CO"]

    for dept_name in departments:
        dept, _ = Department.objects.get_or_create(
            college=college,
            name=dept_name
        )

        for sem in range(1, 9):
            semester, _ = Semester.objects.get_or_create(
                department=dept,
                number=sem
            )

            for section in ["A", "B", "C", "D"]:
                ClassRoomGroup.objects.get_or_create(
                    semester=semester,
                    section_name=section
                )
