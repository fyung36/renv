from rest_framework.views import APIView
from .models import Applicant, Post_Job
from rest_framework.response import Response
from .controllers.AppliciantController import ApplicantController, Postjobcontroller, Applicationcontroller
from django.shortcuts import render
from django.db.models import Q

class Home(APIView):
    def get(self, request):
        applicantController = ApplicantController()
        jobController = Postjobcontroller()
        alljobs = jobController.getAllJobs()
        applycontrollers = Applicationcontroller
        allApplictions = applycontrollers.getApplication(self)
        allApplicants = applicantController.getAllApplicants()
        context = {
            'allApplicants': allApplicants,
            'alljobs': alljobs,
            'allApplication':allApplictions
        }
        return render(request, 'home/index.html', context)

class SearchResultsView(APIView):
    model = Applicant
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Applicant.objects.filter(
            Q(Firstname__icontains=query) | Q(LastName__icontains=query) | Q(Email__icontains=query) | Q(Job_Position__icontains=query)
        )
        context = {
            'filter' : object_list,

        }

        return render(render,'home/index.html', context)

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

class Jobform(APIView):
    def get(self, request):
        context = {
            'result': 'default name'
        }
        return render(request, 'Post-a-job/index.html', context)

class AddJob(APIView):

    def get(self, request):
        context = {
            'result': 'the result'
        }
        return Response(context)

    def post(self, request, format=None):
        postjobData = request.data['JobData']
        postjobcontroller = Postjobcontroller()
        addedJobs = postjobcontroller.Addjobs(postjobData)
        return addedJobs
