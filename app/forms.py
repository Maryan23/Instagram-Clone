from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Profile 
        
class UploadImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')
