# Generated by Django 3.2.9 on 2022-01-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bien_immo',
            fields=[
                ('idOriginel', models.IntegerField(primary_key=True, serialize=False)),
                ('id_lot', models.TextField()),
                ('nb_piece', models.IntegerField()),
                ('typologie', models.TextField()),
                ('prix_tva_reduite', models.FloatField()),
                ('prix_tva_normale', models.FloatField()),
                ('prix_HT', models.FloatField()),
                ('prix_m2_HT', models.FloatField()),
                ('prix_m2_TTC', models.FloatField()),
                ('orientation', models.TextField()),
                ('exterieur', models.BooleanField()),
                ('balcony', models.BooleanField()),
                ('garden', models.BooleanField()),
                ('parking', models.IntegerField()),
                ('ville', models.TextField()),
                ('departement', models.IntegerField()),
                ('date_fin_programme', models.TextField()),
                ('adresse_entiere', models.TextField()),
                ('date_extraction', models.DateField()),
            ],
        ),
    ]
