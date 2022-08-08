
from email.policy import HTTP
from http.client import HTTPResponse
from django.http import HttpResponse

from django.shortcuts import render

#from proyectoFinal.films.models import Film



def resenas(request):
    return render(request, 'reviews-list.html', context={})

def home(request):
    return render(request, 'base.html', context={})


