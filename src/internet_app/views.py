#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, "internet_app/index.html")

def maps(request):
    return render(request, "internet_app/maps.html")

def modification(request):
    return render(request, "internet_app/modification.html")





