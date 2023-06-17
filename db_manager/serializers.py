from rest_framework import serializers
from db_manager.models import Patients

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ('OpNumber','PatientName','Weight','Age','Sex','Address')