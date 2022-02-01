from django.db import models

# Create your models here.


class Student(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField(max_length=10)
    Address = models.TextField()
    Grade = models.CharField(max_length=10)
    Major = models.CharField(max_length=20)

    def __str__(self):
        return self.name