from django.urls import re_path
from db_manager import views

urlpatterns = [
    re_path(r'^patient$',views.patientApi),
    re_path(r'^patient/([0-9]+)$',views.patientApi)
]