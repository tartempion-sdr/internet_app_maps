#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "internet_app/index.html")

def inscription(request):
    form=UserCreationForm(request.POST)
    context={'form':form}
    return render(request, "internet_app/inscription.html")


@login_required(login_url="/compte/acces")

def modification(request):

    return render(request, "internet_app/modification.html")

@login_required(login_url="/compte/acces")
def maps(request):
    return render(request, "internet_app/maps.html")




