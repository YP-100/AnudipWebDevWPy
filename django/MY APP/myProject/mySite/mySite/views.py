from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def home(request):
    return render(request, 'home.html',{})