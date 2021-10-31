from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

User=get_user_model()

#i want to use 1 frm to create 2 different models
class ProfileForm(forms.ModelForm):
    first_name=forms.CharField(required=False) #not related to profile, but to user
    last_name=forms.CharField(required=False)
    email=forms.CharField(required=False)

    class Meta:
        model=Profile
        fields=['location','about_me', 'profile_image']
