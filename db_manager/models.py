from django.db import models

# Create your models here.
class Patients(models.Model):
    # GenderChoices = [
    #     ('M','Male')
    #     ('F','Female')
    # ]
    OpNumber = models.IntegerField(primary_key=True)
    PatientName = models.TextField(max_length=255)
    Weight = models.IntegerField()
    Age = models.IntegerField()
    Sex = models.TextField(max_length=255)
    Address = models.TextField(max_length=500)
    AdmissionDate = models.DateField()