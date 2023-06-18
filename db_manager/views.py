from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#from django.middleware.csrf import get_token
#from django.middleware import csrf

from db_manager.models import Patients
from db_manager.serializers import PatientSerializer
from db_manager.forms import SignUpForm
#from db_manager.cookys import 


# Create your views here.
@csrf_exempt
#@csrf_protect
#@ensure_csrf_cookie
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


def home(request):
    #check user login request
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #do the auth
        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successful Login')
            return redirect('home')
        else:
            messages.success(request,'Login Failed')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out')
    return redirect('home')

def new_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Successful Registration')
            return redirect('home')
    else:
        form = SignUpForm
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form': form})