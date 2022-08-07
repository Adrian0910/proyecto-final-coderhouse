from django.shortcuts import render

# Create your views here.
from films.forms import Form_films

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
            pass 
            return redirect(Form_films)

    elif request.method == 'GET':
        form = Form_films()
        context = {'form':form}
        return render(request, 'film.html', context=context)




    

