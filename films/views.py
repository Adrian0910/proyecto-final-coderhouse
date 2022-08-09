from msilib.schema import Media
from django.shortcuts import render, redirect
from films.forms import Form_films
from films.models import Film


def create_film(request):
    
    if request.method == 'POST':
        form = Form_films(request.POST)

        if form.is_valid():
            Film.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                year = form.cleaned_data['year'],
                director = form.cleaned_data['director'],
                actors = form.cleaned_data['actors'],
                description = form.cleaned_data['description'],
                
            )  
            return redirect (list_films)

    elif request.method == 'GET':
        form = Form_films()
        context = {'form':form}
        return render(request, 'film.html', context=context)



def list_films(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'list_films.html', context=context)



    