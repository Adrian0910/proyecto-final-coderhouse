from django.shortcuts import render, redirect
from reviews.forms import Form_reviews
from reviews.models import Reviews
from django.views.generic import DetailView, DeleteView

def create_review(request):

    if request.method == 'POST':
        form = Form_reviews(request.POST)

        if form.is_valid():
            Reviews.objects.create(
                image=form.cleaned_data['image'],
                name=form.cleaned_data['name'],
                rating=form.cleaned_data['rating'],
                review=form.cleaned_data['review'],

            )
            return redirect (list_reviews)

    elif request.method == 'GET':
        form = Form_reviews()
        context = {'form': form}
        return render(request, 'reviews.html', context=context)


def list_reviews(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'list_reviews.html', context=context)

def delete_review(request, pk):
    if request.method == 'GET':
        reviews = Reviews.objects.get(pk=pk)
        context = {'reviews': reviews}
        return render(request, 'delete_review.html', context=context)
    elif request.method == 'POST':
        reviews = Reviews.objects.get(pk=pk)
        reviews.delete()
    
        return redirect (list_reviews)
    

class Detail_review(DetailView):
    model = Reviews
    template_name= 'detail_review.html'

def update_review(request, pk):
    if request.method == 'POST':
        form = Form_reviews(request.POST)
        if form.is_valid():
            reviews = Reviews.objects.get(id=pk)
            reviews.name = form.cleaned_data['name']
            reviews.rating = form.cleaned_data['rating']
            reviews.review = form.cleaned_data['review']
           
            return redirect(list_reviews)

    elif request.method == 'GET':
        reviews= Reviews.objects.get(id=pk)

        form = Form_reviews(initial={
            'name': reviews.name,
            'rating': reviews.rating,
            'review': reviews.review,
            })
        context = {'form': form}
        return render(request, 'update_review.html', context=context)
