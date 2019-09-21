from .models import Applicant
from rest_framework import serializers

class Applicantserializers(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = ('FirstName','LastName', 'Email', 'Age', 'Job_Position')