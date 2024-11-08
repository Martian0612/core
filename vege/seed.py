from faker import Faker
from vege.models import *
fake = Faker()
import random

def create_subject_marks() -> None:
    try:

        student_obj = Student.objects.all()
        for stu in student_obj:
            subject_obj = Subject.objects.all()
            for sub in subject_obj:

                # It was not working because, we defined sub_marks in this manner.
                # sub_marks = random.randint(0,101)

                # And when we create object using 'Create' method then we donot need to save it by creating and obj (thing.)
                
                SubjectMarks.objects.create(student = stu, subject = sub, marks = random.randint(0,101))

    except Exception as e:
        print(e)

def seed_db(n = 10)->None:
    for _ in range(n):
        depart_name_ls = Department.objects.all()
        depart_index = random.randint(0,len(depart_name_ls)-1)

        department = depart_name_ls[depart_index]
        student_id = f"STU-0{random.randint(100,999)}"
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(18,30)
        student_address = fake.address()

        student_id_obj = StudentID.objects.create(student_id = student_id)

        Student.objects.create(
            department = department,
            student_id = student_id_obj,student_name = student_name ,student_email = student_email,student_age = student_age,student_address = student_address)