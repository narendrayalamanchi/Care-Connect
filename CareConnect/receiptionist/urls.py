
from django.urls import path, include,re_path  
from . import views
from django.contrib.auth import views as auth_views

app_name="receptionist"

urlpatterns = [
    path("", views.home, name="index"),
    path("receptionist/home/", views.home, name="home"),

    path('receptionist/login/', views.receptionist_login, name='receptionistLogin'),

    path("patientinformation/", views.patientinformation, name="patientinformation"),
    path("patientlist/", views.patientlist, name="patientlist"),

    path("doctorinformation/", views.doctorinformation, name="doctorinformation"),
    path("doctorlist/", views.doctorlist, name="doctorlist"),

    path("doctorlist/delete/<int:pk>", views.doctor_delete, name="doctor_delete"),
    path("patientlist/delete/<int:pk>", views.patient_delete, name="patient_delete"),
    path("hospitallist/delete/<int:pk>", views.hospital_delete, name="hospital_delete"),


    path('patientlist/update/<int:pk>', views.PatientUpdate.as_view(), name='patientlist_update'),
    path('doctorlist/update/<int:pk>', views.DoctorUpdate.as_view(), name='doctorlist_update'),
    path('hospitallist/update/<int:pk>', views.HospitalUpdate.as_view(), name='hospitallist_update'),


    path("hospitalinformation/", views.hospitalinformation, name="hospitalinformation"),
    path("hospitallist/", views.hospitallist, name="hospitallist"),

    path('appointment/', views.appointment_list, name='appointment_list'),
    
    path('update/<int:pk>/', views.appointment_update, name='appointment_update'),
    path('delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),

    path('doctor_login/', auth_views.LoginView.as_view(template_name='registration/doctor_login.html'), name='doctor_login'),

    path('doctor_appointment_view/', views.doctor_appointment_view, name='doctor_appointment_view'),

     path("logout/", views.logout_view, name="logout"),
]