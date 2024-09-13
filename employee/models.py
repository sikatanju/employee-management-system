from django.core.validators import RegexValidator

from django.db import models

# Create your models here.

class Employee(models.Model):        
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15,unique=True)
    salary = models.PositiveIntegerField()
    designation = models.CharField(max_length=255)
    description = models.TextField()