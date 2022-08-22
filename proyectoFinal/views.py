
from django.shortcuts import render
from films.models import Film
from reviews.models import Reviews
from tv_shows.models import Tv_shows
#from proyectoFinal.films.models import Film


def home(request):
    return render(request, 'base.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def pages(request):
    return render(request, 'pages.html', context={})

def resenas(request):
    return render(request, 'reviews-list.html', context={})


def search_catalog(request):
    search = request.GET['search']
    catalog = Tv_shows.objects.filter(name__icontains=search)
    catalogM = Film.objects.filter(name__icontains=search)
    reviews = Reviews.objects.filter(name__icontains=search)
    context = {
        'catalog':catalog,
        'catalogM':catalogM,
        'reviews':reviews,
        }
    return render(request, 'search-catalog.html', context=context)


