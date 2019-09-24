from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.



class Applicant(models.Model):
    """ Applicant profile in our app """

    def __str__(self):
        return"{} {}".format(self.FirstName, self.LastName)

    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250, unique=True)
    Age = models.IntegerField(default=0)
    Job_Position = models.CharField(max_length=250)



class Post_Job(models.Model):

    Job_title = models.CharField(max_length=250)
    Job_Description = models.TextField()

    applicants = models.ManyToManyField(Applicant,through='Applications')

    def __str__(self):
         return "{}".format(self.Job_title)

class Applications(models.Model):

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    postjob = models.ForeignKey(Post_Job, on_delete=models.CASCADE)
