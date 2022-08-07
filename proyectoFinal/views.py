
from django.http import HttpResponse

from django.shortcuts import render #render de htmls


def prueba(request):
    return HttpResponse("Hola mundo")

def resenas(request):
    return render(request, 'resenas.html', context={})


