from rest_framework import serializers
from .models import Applicant
from django.contrib.auth.models import User

class ApplicantFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = ('FirstName', 'LastName', 'Email', 'Age', 'Job_Position')
        # fields = '__all__'
