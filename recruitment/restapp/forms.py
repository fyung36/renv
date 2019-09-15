from .models import Applicant
from django import forms

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['FirstName', 'LastName', 'Email','Age','Job_Position']
