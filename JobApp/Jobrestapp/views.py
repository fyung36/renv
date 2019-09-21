from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Applicantserializers
from .models import Applicant
from rest_framework.views import APIView

# Create your views here.

# class Home(APIView):
class Home(viewsets.ModelViewSet):

    queryset = Applicant.objects.all().order_by('-FirstName')
    serializer_class = Applicantserializers

class Add
    # def get(self, request):
    #     applicantController = ApplicantController()
    #     allApplicants = applicantController.getAllApplicants()
    #     context = {
    #         'allApplicants': allApplicants
    #     }
    #     return render(request, 'home/index.html', context)
