

from django.shortcuts import render, redirect
from tv_shows.forms import Form_tv_shows
from tv_shows.models import Tv_shows
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required


@login_required
def create_tv_show(request):
    if request.method == 'POST':
        form = Form_tv_shows(request.POST,  request.FILES)

        if form.is_valid():
            Tv_shows.objects.create(
                image=form.cleaned_data['image'],
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                year=form.cleaned_data['year'],
                director=form.cleaned_data['director'],
                actors=form.cleaned_data['actors'],
                description=form.cleaned_data['description'],

            )
            return redirect(list_tv_shows)

    elif request.method == 'GET':
        form = Form_tv_shows()
        context = {'form': form}
        return render(request, 'tv_shows.html', context=context)
    # return redirect('login')


def list_tv_shows(request):
    tv_shows = Tv_shows.objects.all()
    context = {
        'tv_shows': tv_shows
    }
    return render(request, 'list_tv_shows.html', context=context)


@login_required
def delete_tv_show(request, pk):
    if request.method == 'GET':
        tv_shows = Tv_shows.objects.get(pk=pk)
        context = {'tv_shows': tv_shows}
        return render(request, 'delete_tv_show.html', context=context)
    elif request.method == 'POST':
        tv_shows = Tv_shows.objects.get(pk=pk)
        tv_shows.delete()
        return redirect(list_tv_shows)

class Detail_tv_show(DetailView):
    model = Tv_shows
    template_name= 'detail_tv_show.html'


def update_tv_show(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            form = Form_tv_shows(request.POST)
            if form.is_valid():
                tv_shows = Tv_shows.objects.get(id=pk)
                tv_shows.name = form.cleaned_data['name']
                tv_shows.price = form.cleaned_data['price']
                tv_shows.year = form.cleaned_data['year']
                tv_shows.director = form.cleaned_data['director']
                tv_shows.actors = form.cleaned_data['actors']
                tv_shows.description = form.cleaned_data['description']
                tv_shows.save()

                return redirect(list_tv_shows)

        elif request.method == 'GET':
            tv_shows = Tv_shows.objects.get(id=pk)

            form = Form_tv_shows(initial={
                'name': tv_shows.name,
                'price': tv_shows.price,
                'year': tv_shows.year,
                'director': tv_shows.director,
                'actors': tv_shows.actors,
                'description': tv_shows.description, })
            context = {'form': form}
            return render(request, 'update_tv_show.html', context=context)
    else:
        return redirect('login')