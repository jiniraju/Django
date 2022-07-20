from django.db import models

# Create your models here.

class studentDetails(models.Model):
    student_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    joining_date=models.DateField()
    email=models.EmailField()
    qualification=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)