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
    number = models.IntegerField(max_length=6)
    tel = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name
