from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    email=models.EmailField(max_length=254, unique=True)
    phone=models.CharField(max_length=50, unique=True)
    

