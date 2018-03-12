from django import forms
from myproject.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
	fields = ['fullname','lastname', 'email','phone', 'subject', 'message']


class EnrollmentForm(forms.ModelForm):

	class Meta:
		model = Enrollment
		fields = ['name', 'phone1', 'phone2', 'address', 'aadhar_card', 'vehicle_no', 'vehicle_type', 'attach_files', 'driving_license', 'cbook',]

class Fm16Form(forms.ModelForm):

	class Meta:
		model = Fm16
		fields = '__all__'
