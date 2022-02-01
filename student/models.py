from django.db import models
from django.urls import reverse

# Create your models here.


class Student(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Address = models.CharField(max_length=200)
    Grade = models.CharField(max_length=10)
    Major = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.Name