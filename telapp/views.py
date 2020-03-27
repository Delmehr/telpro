from django.shortcuts import render
from django.core.paginator import Pginator
from django.db.models import Q
#from django.http import HttpResponse
# Create your views here.

from telapp.models import Person, Telnum

def index(request):
    all_persons = Person.objects.all()
    all_telnum = Telnum.objects.all()
    paginator = paginator(all_persons, 2)
    page = request.GET.get('page')
    persons = paginator.get_page(page)
    context = {
         'persons': persons,
        #'person_list': all_persons,
        'tel_list': all_telnum,
        'page_title': "List of all Persons"

    }
    return render(request, "telapp/index.html", context)

def list(request):

    all_persons = Person.objects.all()
    all_telnum =  Telnum.objects.all()

    context = {

    'person_list': all_persons,
    'tel_list': all_telnum,

    }

    return render(request, "telapp/testindex.html", context)

def search(request):

    template = 'telapp/search.html'

    query = request.GET.get('q')

    results = Person.objects.filter(Q(f_name__icontains=query) | Q(l_name__icontains=query))

    context = {
              'items': results,

    }

    return render(request, template, context)
