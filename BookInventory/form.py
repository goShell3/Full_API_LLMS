from django import forms
from django.contrib.auth.models import User, Login, Logout

class RegisterForm(forms.ModelForm):
    class Meta:
        verbose_name = 'login'
    name = forms.CharField(widget=forms.PasswordInput,label="Name 👉... ", max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput,label="Pass 🔐🤐 .. ", max_length=100, required=True)


    pass;

