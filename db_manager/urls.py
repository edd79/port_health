from django.urls import re_path,path
from db_manager import views

urlpatterns = [
    re_path(r'^patient$',views.patientApi),
    re_path(r'^patient/([0-9]+)$',views.patientApi),
    path('',views.user_login, name= 'login'),
    # path('',views.home, name= 'home'),
    # path('logout/',views.user_logout, name='logout'),
    # path('register/',views.new_user, name='register')
]