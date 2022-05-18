from dataclasses import fields
from pyexpat import model
from django import forms
from .models import signup_master,notes,contactdata

class signupForm(forms.ModelForm):
    class Meta:
        model=signup_master
        fields='__all__'

class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model=contactdata
        fields='__all__'
