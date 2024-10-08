from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *

@receiver(post_save, sender=User)
def create_receptionist(sender, instance, created, **kwargs):
    if created:
        Receptionist.objects.create(user=instance)

@receiver(post_save, sender=Patient)
def create_or_update_patient_profile(sender, instance, created, **kwargs):
    if created:
        PatientProfile.objects.create(patient=instance)
    else:
        instance.Doctor.save()