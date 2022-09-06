from msilib.schema import Media
from django.shortcuts import render, redirect
from films.forms import Form_films
from films.models import Film
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required



@login_required
def create_film(request):
    
    if request.method == 'POST':
        form = Form_films(request.POST, request.FILES)

        if form.is_valid():
            Film.objects.create(
                image = form.cleaned_data['image'],
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

@login_required
def delete_film(request, pk):
    if request.method == 'GET':
        film = Film.objects.get(pk=pk)
        context = {'film': film}
        return render(request, 'delete_film.html', context=context)
    elif request.method == 'POST':
        film = Film.objects.get(pk=pk)
        film.delete()
        return redirect(list_films)

class Detail_film(DetailView):
    model = Film
    template_name= 'detail_film.html'


def update_film(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = Form_films(request.POST)
            if form.is_valid():
                film = Film.objects.get(id=pk)
                film.name = form.cleaned_data['name']
                film.price = form.cleaned_data['price']
                film.year = form.cleaned_data['year']
                film.director = form.cleaned_data['director']
                film.actors = form.cleaned_data['actors']
                film.description = form.cleaned_data['description']
                film.save()

                return redirect(list_films)

        elif request.method == 'GET':
            film = Film.objects.get(id=pk)

            form = Form_films(initial={
                'name': film.name,
                'price': film.price,
                'year': film.year,
                'director': film.director,
                'actors': film.actors,
                'description': film.description, })
            context = {'form': form}
            return render(request, 'update_film.html', context=context)
    else:
        return redirect('login')
