from django.db import models

# Create your models here.
from django.core.mail import send_mail
from django.conf import settings

def envoyer_email_confirmation(reservation):
    # Créer un message de confirmation de réservation
    subject = "Confirmation de réservation"
    message = f"Bonjour {reservation.name},\n\n"
    message += f"Votre réservation a été confirmée pour le {reservation.date} à {reservation.time}.\n"
    message += f"Nombre de personnes : {reservation.number}\n\n"
    message += "Merci de votre réservation !"
    
    # Envoyer l'email à l'adresse de la réservation
    send_mail(
        subject,  # Sujet
        message,  # Corps du message
        settings.EMAIL_HOST_USER,  # Expéditeur (ton adresse email)
        [reservation.email],  # Destinataire (email de la réservation)
        fail_silently=False,  # Si une erreur se produit, elle sera levée
    )
