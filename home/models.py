from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length= 100)
    age = models.IntegerField(default = 4)
    email = models.EmailField(null= True, blank = True)
    address = models. TextField(null= True, blank = True)
    # assume file and image field to be deleted, 
    # in case of image field, upload_to -> means where it will get store after getting into the database.
    # image = models.ImageField()
    # file = models.FileField() -> let say we remove it from the database


class Car(models.Model):
    car_name = models.CharField(max_length = 500)
    speed = models.IntegerField()
    

    def __str__(self):
        return self.car_name