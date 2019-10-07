from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

    class Meta:
    	ordering = ['name']

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    is_adult = models.BooleanField(default=True)
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
    	return self.name

    class Meta:
    	ordering = ['name']

