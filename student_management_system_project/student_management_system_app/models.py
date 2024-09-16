from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    marks = models.FloatField()
