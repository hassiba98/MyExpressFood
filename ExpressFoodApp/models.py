from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class Category (models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

class Meal (models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.title

class Commande (models.Model):
    items = models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    prenom = models.CharField(max_length=300)
    email = models.EmailField()
    adress = models.CharField(max_length=300)
    ville = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']

