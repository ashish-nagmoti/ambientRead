from django import forms 
from .models import UserFile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']