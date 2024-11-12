# vim: set fileencoding=utf-8 :
from django.contrib import admin
import Index.models as models  # Importation correcte des modèles depuis Index

# Actions personnalisées
def accepter_reservation(modeladmin, request, queryset):
    queryset.update(status='acceptée')

import Index.models as models
def refuser_reservation(modeladmin, request, queryset):
    queryset.update(status='refusée')

# Configuration de ReservationAdmin
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'time', 'email', 'number', 'tel', 'status')
    list_filter = ('status',)  # Filtre pour afficher par statut
    actions = [accepter_reservation, refuser_reservation]  # Actions à ajouter pour l'admin

# Configuration de CategoriesAdmin
class CategoriesAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name',)


# Configuration de MenuAdmin
class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'Categories', 'Description')
    list_filter = ('Categories', 'id', 'name', 'price', 'Description')
    search_fields = ('name',)


class ReservationAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'date', 'time', 'email', 'number', 'tel')
    list_filter = ('date', 'id', 'name', 'time', 'email', 'number', 'tel')
    search_fields = ('name',)


# Fonction pour enregistrer un modèle
def _register(model, admin_class):
    admin.site.register(model, admin_class)
    if not admin.site.is_registered(model):
        admin.site.register(model, admin_class)

# Enregistrement des modèles avec leur admin
_register(models.Categories, CategoriesAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Reservation, ReservationAdmin)
