from rest_framework.views import APIView
from rest_framework.response import Response
from .controllers.ApplicantController import ApplicantController
from django.shortcuts import render
from rest_framework import filters
# Create your views here.

class Home(APIView):
    def get(self, request):
        applicantController = ApplicantController()
        allApplicants = applicantController.getAllApplicants()
        context = {
            'allApplicants': allApplicants
        }
        return render(request, 'home/index.html', context)

class Search(APIView):
    def get(self, request):
        searchBasedOn = request.GET.get('searchBasedOn', '')
        searchInputValue = request.GET.get('searchInputValue', '')
        applicantController = ApplicantController()
        filters = {
            searchBasedOn: searchInputValue
        }
        allApplicants = applicantController.SearchForApplicants(searchBasedOn, searchInputValue)
        context = {
            'allApplicants': allApplicants,
            'searchResult': True,
            'filters': filters
        }
        return render(request, 'home/index.html', context)

class ApplicantForm(APIView):
    def get(self, request):
        context = {
            'result': 'default name'
        }
        return render(request, 'applicant-form/index.html', context)

class AddApplicant(APIView):

    def get(self, request):
        context = {
            'result': 'the result'
        }
        return Response(context)

    def post(self, request, format=None):
        applicantData = request.data['applicantData']
        applicantController = ApplicantController()
        addedApplicant = applicantController.AddApplicant(applicantData)
        return addedApplicant
