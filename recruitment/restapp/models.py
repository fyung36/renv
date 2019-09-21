from django.db import models

# Create your models here.

class Applicant(models.Model):

    def __str__(self):
        return self.FirstName

    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250)
    Job_Position = models.CharField(max_length=250)
    # date_of_birth = models.DateField()
    Age = models.IntegerField(default=0)

  #  def age(self):
    # import datetime
    # dob = self.date_of_birth
    # tod = datetime.date.today()
    # my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
#      return my_age

