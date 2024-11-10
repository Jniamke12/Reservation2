from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse,HttpRequest



# Create your views here.

def Index (request):
    Menu = models.Menu.objects.all()
    
    data = {
        'menu': Menu,
    }
    return render(request, 'index.html', data)

def Reservation (request):
    if request.method == 'POST':
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
        return redirect('Index')

    