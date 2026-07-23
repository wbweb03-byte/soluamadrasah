from .models import Student

def generate_admission_number(session):
    year = session.split("-")[0]

    last = (
        Student.objects.filter(
            admission_no__startswith=f"SMDQ-{year}-No-"
        )
        .order_by("-admission_no")
        .first()
    )

    if last:
        last_no = int(last.admission_no.split("-")[-1])
    else:
        last_no = 0

    return f"SMDQ-{year}-No-{last_no + 1:04d}"


def generate_registration_number():
    last = Student.objects.filter(
        registration_no__startswith="STU1977"
    ).order_by("-registration_no").first()

    if last:
        last_no = int(last.registration_no.split("-")[-1])
    else:
        last_no = 0

    return f"STU1977-{last_no + 1:04d}"