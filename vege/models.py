from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank= True)
    receipe_name = models.CharField(max_length = 100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="static/vege/img", null= True, blank = True)
    receipe_view_count = models.IntegerField(default= 1)

    def __str__(self):
        return self.receipe_name
    
class Department(models.Model):
    department = models.CharField(max_length= 100, unique = True)

    def __str__(self)-> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length= 100, unique= True)

    def __str__(self)-> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name= "depart", on_delete = models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name= "studentid",on_delete = models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField(unique= True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()

    def __str__(self)->str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        # Verbose name is human readable name of the class
        verbose_name = "student"

class Subject(models.Model):
    subject_name = models.CharField(max_length= 300)
    subject_code = models.CharField(max_length= 50)

    class Meta:
        ordering = ['subject_code']

    def __str__(self):
        return self.subject_name
    
# how to define related name, MEANS HOW TO THINK THEIR NAME
class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name = "studentmarks", on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = "subjectmarks",on_delete= models.CASCADE)
    marks = models.IntegerField()

    class Meta:

        unique_together = ['student', 'subject']

    def __str__(self):
        return f" {self.student.student_name} {self.subject.subject_name}"
    

class rank(models.model):
    pass