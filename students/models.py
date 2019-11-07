from django.db import models
from django.conf import settings

GENDER_LIST=[
    ("Male", "Male"),
    ("Female", "Female")
]
DEPARTMENT_LIST = [
    ("Mech", "Mechanical Engineering"),
    ("Civil", "Civil Engineering"),
    ("CSE", "Computer Science Engineering"),
    ("IT", "Information Technology"),
    ("ECE", "Electronics & Communications Engineering"),
    ("EEE", "Electrical & Electronics Engineering")
]

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_LIST)
    dob = models.DateField()
    dept = models.CharField(max_length=50, choices=DEPARTMENT_LIST)
    remarks = models.TextField

    def __str__(self):
        return self.name
