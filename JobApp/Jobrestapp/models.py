from django.db import models

# Create your models here.

class Applicant(models.Model):

    def __str__(self):
        return self.FirstName

    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250, unique=True)
    Age = models.IntegerField(default=0)
    Job_Position = models.CharField(max_length=250)

