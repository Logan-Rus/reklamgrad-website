from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('collections/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('works/<int:work_id>/', views.work_detail, name='work_detail'),
    path('works/', views.all_works, name='all_works'),
    path('collections/', views.all_collections, name='all_collections'),
]



