from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render, redirect
from tv_shows.forms import Form_tv_shows
from tv_shows.models import Tv_shows
from django.http import HttpResponse


def create_tv_show(request):
    
    if request.method == 'POST':
        form = Form_tv_shows(request.POST)

        if form.is_valid():
            Tv_shows.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                year = form.cleaned_data['year'],
                director = form.cleaned_data['director'],
                actors = form.cleaned_data['actors'],
                description = form.cleaned_data['description'],
                
            )  
            return redirect (list_tv_shows)

    elif request.method == 'GET':
        form = Form_tv_shows()
        context = {'form':form}
        return render(request, 'tv_shows.html', context=context)


def list_tv_shows(request):
    tv_shows = Tv_shows.objects.all()
    context = {
        'tv_shows': tv_shows
    }
    return render(request, 'list_tv_shows.html', context=context)


def search_catalog(request):
    search = request.GET['search']
    catalog = Tv_shows.objects.filter(name__icontains=search)
    context = {'catalog':catalog}
    return render(request, 'search-catalog.html', context=context)
