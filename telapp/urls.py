from django.urls import path
from . import views

app_name = 'telapp'
urlpatterns = [

    path('', views.index, name='index_all'),
    path('search/', views.search, name='search_all'),
    path('add/', views.add_person, name='add_person')

        ]
