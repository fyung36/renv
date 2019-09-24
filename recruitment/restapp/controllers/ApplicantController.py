from rest_framework.response import Response
from ..models import Applicant
from ..forms import ApplicantForm
from ..serializers import ApplicantFormSerializer

class ApplicantController():

    def getAllApplicants(self):
        applicants = Applicant.objects.all()
        return applicants

    def SearchForApplicants(self, searchBasedOn, searchInputValue):
        filters = {
            searchBasedOn: searchInputValue
        }
        searchedApplicants = Applicant.objects.filter(**filters)
        return searchedApplicants

    def AddApplicant(self, applicantData):
        formData = ApplicantForm(applicantData)
        if formData.is_valid():
            applicant = Applicant(
                FirstName=applicantData['FirstName'],
                LastName=applicantData['LastName'],
                Email=applicantData['Email'],
                Age=applicantData['Age'],
                Job_Position=applicantData['Job_Position']
            )
            applicant.save()
            applicantFiltered = Applicant.objects.filter(pk=applicant.pk)
            serializer = ApplicantFormSerializer(applicantFiltered, many=True)
            return Response(serializer.data)
        return Response("form is not valid")