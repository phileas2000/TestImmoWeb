from django.db import models

# Create your models here.

class Bien_immo(models.Model):
    idOriginel = models.IntegerField(primary_key=True)
    id_lot = models.TextField(null=True, blank=True)
    nb_piece = models.IntegerField(null=True, blank=True)
    typologie =	models.TextField(null=True, blank=True)
    prix_tva_reduite =	models.FloatField(null=True, blank=True)
    prix_tva_normale =	models.FloatField(null=True, blank=True)
    prix_HT	= models.FloatField(null=True, blank=True)
    prix_m2_HT = models.FloatField(null=True, blank=True)	
    prix_m2_TTC	= models.FloatField(null=True, blank=True)
    orientation	= models.TextField(null=True, blank=True)
    exterieur = models.BooleanField(null=True, blank=True)
    balcony = models.BooleanField(null=True, blank=True)
    garden = models.BooleanField(null=True, blank=True)
    parking	= models.IntegerField(null=True, blank=True)
    ville = models.TextField(null=True, blank=True)
    departement	= models.IntegerField(null=True, blank=True)
    date_fin_programme = models.TextField(null=True, blank=True)
    adresse_entiere = models.TextField(null=True, blank=True)
    date_extraction = models.DateField(null=True, blank=True)
    