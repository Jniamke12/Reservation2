from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse,HttpRequest
from django.db.models import F, Value, IntegerField
from django.db.models.functions import Abs



# Create your views here.

def Index (request):
    Menu = models.Menu.objects.all()
    
    data = {
        'menu': Menu,
    }
    return render(request, 'index.html', data)

def Reservation (request):

    # Récupérer le nombre de personnes depuis le formulaire
    personne = int(request.POST.get('number'))

    # Rechercher les tables avec un nombre de places proche du nombre de personnes
    tables_proches = models.Table.objects.filter(
    status=False  # Filtrer les tables dont le `status` est `False`
    ).annotate(
    difference=Abs(F('nombre_de_place') - Value(personne, output_field=IntegerField()))
    ).order_by('difference')


    if request.method == 'POST' and tables_proches.exists() :

        nom = request.POST.get('name')
        telephone = request.POST.get('phone')
        date = request.POST.get('date')
        email = request.POST.get('email')
        personne = request.POST.get('number')
        heure = request.POST.get('time')
        reserver = models.Reservation(
            name = nom,
            date = date,
            time = heure,
            tel = telephone,
            email = email,
            number = personne,
        )

        reserver.save()
    else:
        print(tables_proches)

        return redirect('Index')

    