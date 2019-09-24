from .models import Applicant, Post_Job
from rest_framework import serializers

class Applicantserializers(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = ('FirstName','LastName', 'Email', 'Age', 'Job_Position')

class Postserializers(serializers.ModelSerializer):

    class Meta:
        model = Post_Job
        fields = {'Job_title','Job_Description'}