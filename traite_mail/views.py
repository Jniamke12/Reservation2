from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings

def envoyer_email_utilisateur(reservation):
    subject = 'Statut de votre réservation'
    if reservation.status == 'acceptée':
        message = f'Bonjour {reservation.name},\nVotre réservation pour le {reservation.date} à {reservation.time} a été acceptée.'
    elif reservation.status == 'refusée':
        message = f'Bonjour {reservation.name},\nVotre réservation pour le {reservation.date} à {reservation.time} a été refusée.'
    else:
        message = f'Bonjour {reservation.name},\nVotre réservation pour le {reservation.date} à {reservation.time} est en attente.'

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [reservation.email],
        fail_silently=False,
    )

def accepter_reservation(modeladmin, request, queryset):
    queryset.update(status='acceptée')
    for reservation in queryset:
        envoyer_email_utilisateur(reservation)

def refuser_reservation(modeladmin, request, queryset):
    queryset.update(status='refusée')
    for reservation in queryset:
        envoyer_email_utilisateur(reservation)
