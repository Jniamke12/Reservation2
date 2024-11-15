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

def Reservation(request):

    if request.method == 'POST':  # Vérifie que la méthode est POST
        # Récupérer le nombre de personnes depuis le formulaire
        personne = int(request.POST.get('number', 0))  # Valeur par défaut : 0
        
        # Rechercher les tables disponibles avec un nombre de places supérieur ou égal au nombre de personnes
        tables_proches = models.Table.objects.filter(
            status=False,  # Filtrer les tables disponibles (status=False)
            nombre_de_place__gte=personne,  # Ajouter la condition pour le nombre de places supérieur ou égal au nombre de personnes
            nombre_de_place__lte=personne+2
        ).order_by('nombre_de_place')

        if tables_proches.exists():
            # Récupérer les informations du formulaire
            nom = request.POST.get('name')
            telephone = request.POST.get('phone')
            date = request.POST.get('date')
            email = request.POST.get('email')
            heure = request.POST.get('time')

            # Créer et sauvegarder la réservation
            reserver = models.Reservation(
                name=nom,
                date=date,
                time=heure,
                tel=telephone,
                email=email,
                number=personne,
            )
            reserver.save()

            

            # Rediriger vers une page de succès ou afficher un message
            return render(request, 'index.html', {'name': nom})
        else:
            # Aucune table disponible
            return render(request, 'index.html', {'error': "Aucune table disponible pour ce nombre de personnes."})

    # Si la méthode n'est pas POST, redirige vers le formulaire de réservation
    return redirect('Index')


    