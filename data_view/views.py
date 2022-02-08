from django.shortcuts import render
from django.http import HttpResponse
import psycopg2 
import pandas as pd
import csv
#from django.db import models
from datetime import datetime
from .models import Bien_immo






'''
class Bien_immo(models.Model):
    idOriginel = models.IntegerField(primary_key=True)
    id_lot = models.TextField()
    nb_piece = models.IntegerField()
    typologie =	models.TextField()
    prix_tva_reduite =	models.FloatField()
    prix_tva_normale =	models.FloatField()
    prix_HT	= models.FloatField()
    prix_m2_HT = models.FloatField()	
    prix_m2_TTC	= models.FloatField()
    orientation	= models.TextField()
    exterieur = models.BooleanField()
    balcony = models.BooleanField()
    garden = models.BooleanField()
    parking	= models.IntegerField()
    ville = models.TextField()
    departement	= models.IntegerField()
    date_fin_programme = models.TextField()
    adresse_entiere = models.TextField()
    date_extraction = models.DateField()
'''

# Create your views here.
def main(request):
    file=open('static/immo_CSV.csv', 'rb')
    if  file ==None:
        html="<p>Immo_csv non présent!<p><a href=\"../\">Lien vers load_csv</a>"
    else:
        
        html=read_immo()
        
           
    return HttpResponse(html)


def read_immo():
    
    data=pd.read_csv('static/immo_CSV.csv',delimiter=";")
    data=data.head(5)
    #print(data)
    print(data['balcony'])
    data['prix_tva_reduite'] = data['prix_tva_reduite'].fillna(0)
    Bien_immo.objects.all().delete()
    csv_name = "static/immo_CSV.csv"
    data['date_extraction'] =data['date_extraction'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))
    for index,immo in data.iterrows():
     
        immo_obj=Bien_immo(id_lot=immo.loc['id_lot'],nb_piece=immo.loc['nb_piece'],typologie=immo.loc['typologie'],prix_tva_reduite=immo.loc['prix_tva_reduite'],prix_tva_normale=immo.loc['prix_tva_normale'],\
        prix_HT=immo['prix_HT'],prix_m2_HT=immo['prix_m2_HT'],prix_m2_TTC=immo['prix_m2_TTC'],orientation=immo['orientation'],exterieur=immo['exterieur'],balcony=immo['balcony'],garden=immo['garden'],\
        parking=immo['parking'],ville=immo['ville'],departement=immo['departement'],date_fin_programme=immo['date_fin_programme'],adresse_entiere=immo['adresse_entiere'],date_extraction=immo['date_extraction'])
        immo_obj.save()
    filtered=Bien_immo.objects.filter(balcony=False)
    print(filtered.values_list())
    #print(Bien_immo.objects.values_list())
    return "<p id=\'prediction\'>"+str(list(filtered.values_list()))+"</p><a href=\"../\">Lien vers load_csv</a>" 
    
    
