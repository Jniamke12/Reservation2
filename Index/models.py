from django.db import models


# Create your models here.

class Categories(models.Model):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


    
class Menu(models.Model):

    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    Categories = models.ForeignKey("Categories",on_delete=models.CASCADE)
    Description = models.TextField()


    def __str__(self):
        return self.name
    


class Reservation(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    tel = models.CharField(max_length=10)


    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length=100, default="Table inconnue")  # Ajout d'une valeur par défaut
    nombre_de_place = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

