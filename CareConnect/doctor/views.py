from django.shortcuts import render, redirect
from receiptionist.models import Appointment,Doctor
from django.http import JsonResponse, HttpResponse
# from .forms import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    doctor = Doctor.objects.filter(user=request.user).first()
    appointments = Appointment.objects.filter(doctor = doctor)
    return render(request, "doctor/doctor_appointment_view.html", {"appointments": appointments})

def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None and user.groups.filter(name='doctor').exists():
                login(request, user)
                return redirect("doctor:home") 
            else:
                return HttpResponse("You don't have permission to access this page. Please contact staff or admin.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/doctor_login.html', {'form': form})