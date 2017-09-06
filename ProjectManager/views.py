from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request , 'rachel_katz_home.html')

def resume(request):
    return render(request , 'resume_home.html')

def current_project(request):
    return render(request , 'current_project_home.html')

def interests(request):
    return render(request , 'interests.html')