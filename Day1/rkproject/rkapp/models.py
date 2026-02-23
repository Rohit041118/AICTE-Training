from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=200, unique=True)
    role = models.CharField(max_length=100, default='student')

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=200, unique=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
