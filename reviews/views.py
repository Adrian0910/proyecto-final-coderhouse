from django.shortcuts import render, redirect
from reviews.forms import Form_reviews
from reviews.models import Reviews


def create_review(request):
    
    if request.method == 'POST':
        form = Form_reviews(request.POST)

        if form.is_valid():
            Reviews.objects.create(
                name = form.cleaned_data['name'],
                rating = form.cleaned_data['rating'],
                review = form.cleaned_data['review'],
                
            )  
            return redirect (list_reviews)

    elif request.method == 'GET':
        form = Form_reviews()
        context = {'form':form}
        return render(request, 'reviews.html', context=context)



def list_reviews(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'list_reviews.html', context=context)
