from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain
# Create your views here.

from telapp.models import Person, Telnum, ContactForm, TelForm

def index(request):
    all_persons = Person.objects.all()
    all_telnum = Telnum.objects.all()
    paginator = Paginator(all_persons, 10)
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
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match = Person.objects.filter(Q(f_name__icontains=srch) |
                                         (Q(l_name__icontains=srch)))
            catch = Telnum.objects.filter(Q(tel_num__icontains=srch))

            all_tels = Telnum.objects.all()
            all_persons= Person.objects.all()

            if match or catch:
                return render(request, 'telapp/search.html', {'sr':match, 'tl':all_tels, "pers":all_persons,
                                                              'sp':catch})

            else:
                messages.error(request,  'no result found!')

        else:
            return HttpResponseRedirect('/search/')

    return render(request, 'telapp/search.html')

def add_person(request):
    if request.method == 'POST':
        nameform = ContactForm(request.POST)
        if nameform.is_valid(): #and telform.is_valid():
            nameform.save()
            #telform.save()
            return redirect(add_person)

    else:
        nameform = ContactForm
        #telform = TelForm



    context = {
    'nameform':nameform,
    #'telform': telform,
    }
    return render(request, 'telapp/add_person.html', context)

    if request.method =='POST':

        telform  = TelForm(request.POST)
        if telform.is_valid():
            telform.save()
            return redirect(add_person)

    else:
        telform = TelForm

    pontext ={
    'telform': telform,
    }

    return render(request, 'telapp/add_person.html', pontext)
