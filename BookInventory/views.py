from django.shortcuts import render
from .models import *
from .form import RegisterForm
from django.con


def Login_view(request):
    if request.method == "POST":
        pass
    else:
        return render(request, redirect)
