from django.contrib import admin
from vege.models import *
# Register your models here.
# admin.site.register(Receipe)


class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'student_id']

class StudentIDAdmin(admin.ModelAdmin):
    # list_display = ['student_id', 'student__student_name']
    list_display = ['student_id', 'display_student_name']

    def display_student_name(self,obj):
        return  obj.studentid.student_name
        # return ", ".join([id.student_name for id in obj.studentid.all()])
    
admin.site.register(StudentID, StudentIDAdmin)
my_models= [Receipe , Department , Subject]

# my_models= [Receipe , Department , StudentID , Student, StudentAdmin , Subject]
# Registering all the models at one go.
admin.site.register(my_models)

admin.site.register(Student, StudentAdmin)
admin.site.register(SubjectMarks, SubjectMarksAdmin)