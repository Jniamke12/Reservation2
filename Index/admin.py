# vim: set fileencoding=utf-8 :
from django.contrib import admin

import Index.models as models


class CategoriesAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name',)


class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'Categories', 'Description')
    list_filter = ('Categories', 'id', 'name', 'price', 'Description')
    search_fields = ('name',)


class ReservationAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'date', 'time', 'email', 'number', 'tel')
    list_filter = ('date', 'id', 'name', 'time', 'email', 'number', 'tel')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categories, CategoriesAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Reservation, ReservationAdmin)
