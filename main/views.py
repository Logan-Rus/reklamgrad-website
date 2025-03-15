from django.shortcuts import render, get_object_or_404
from .models import Work, Collection

def home(request):
    works = Work.objects.all()
    collections = Collection.objects.all()
    latest_works = Work.objects.all().order_by('id')
    return render(request, 'main/home.html', {
        'works': works,
        'collections': collections,
        'latest_works': latest_works,
    })

def collection_detail(request, collection_id):
    collection = Collection.objects.get(id=collection_id)  # Получаем коллекцию по ID
    latest_works = Work.objects.all().order_by('id')
    return render(request, 'main/collection_detail.html', {'collection': collection, 'latest_works': latest_works})

def all_collections(request):
    collection2 = Collection.objects.all()
    latest_works = Work.objects.all().order_by('id')
    return render(request, 'main/all_collections.html', {'collection2': collection2, 'latest_works': latest_works})

def work_detail (request, work_id):
    latest_works = Work.objects.all().order_by('id')
    work = Work.objects.get(id=work_id) # Получаем одну работу по ID
    return render(request, 'main/work_detail.html', {'work': work, 'latest_works': latest_works})

def all_works(request):
    latest_works = Work.objects.all().order_by('id')
    work2 = Work.objects.all()
    return render(request, 'main/all_works.html', {'work2': work2, 'latest_works': latest_works})
