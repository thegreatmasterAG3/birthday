from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from django.contrib import messages
from django.conf import settings
import os




@login_required(login_url='/')
def HOME(request):
    return render(request,'Admin/home.html')


# @login_required(login_url='/')
# def INDEX(request):
#     return render(request,'Admin/index.html')


from django.shortcuts import render
from django.contrib.staticfiles import finders
import json

@login_required(login_url='/')
def INDEX(request):
    return render(request, 'Admin/index.html')

@login_required(login_url='/')
def INDEX1(request):
    return render(request,'Admin/index1.html')
