from django.db import models
from django.db.models.fields.related import ForeignKey


class CategoryFoot(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class ProductFoot(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    category = ForeignKey(CategoryFoot, on_delete=models.CASCADE, related_name='categories_foot')
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.titre


class CommandeFoot(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    date_commande = models.DateTimeField(auto_now_add=True)
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom
