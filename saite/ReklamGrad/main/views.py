from django.shortcuts import render
from .models import Review, Collection

def home(request):
    reviews = Review.objects.all()
    collections = Collection.objects.all()
    return render(request, 'main/home.html', {
        'reviews': reviews,
        'collections': collections
    })
