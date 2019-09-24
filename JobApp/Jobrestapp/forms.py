from .models import Applicant,Post_Job
from django import forms

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['FirstName', 'LastName', 'Email', 'Age', 'Job_Position']

class Postjobform:
    class Mera:
        model = Post_Job
        fields = {'Job_title','Job_Description'}