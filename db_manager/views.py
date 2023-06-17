from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from db_manager.models import Patients
from db_manager.serializers import PatientSerializer

# Create your views here.
@csrf_exempt
def patientApi(request,id = 0):
    if request.method == 'GET':
        patients = Patients.objects.all()
        patient_serializer = PatientSerializer(patients,many=True)
        return JsonResponse(patient_serializer.data,safe=False)
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(data=patient_data) 
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
        patient_data = JSONParser().parse(request)
        patient = Patients.objects.get(OpNumber = patient_data['OpNumber'])
        patient_serializer = PatientSerializer(patient, data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse('Updated Succesfully',safe=False)
        return JsonResponse('Update Failed',safe=False)
    elif request.method == 'DELETE':
        patient = Patients.objects.get(OpNumber = id)
        patient.delete()
        return JsonResponse('Deleted Successfully',safe=False)
