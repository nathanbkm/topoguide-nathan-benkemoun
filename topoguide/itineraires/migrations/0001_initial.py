# Generated by Django 4.0.4 on 2022-04-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='titre')),
                ('start_point', models.CharField(max_length=200, verbose_name='point de départ')),
                ('description', models.CharField(max_length=400)),
                ('start_alt', models.FloatField(verbose_name='altitude de départ (m)')),
                ('alt_min', models.FloatField(verbose_name='altitude min (m)')),
                ('alt_max', models.FloatField(verbose_name='altitude max (m)')),
                ('elevation_gain', models.FloatField(verbose_name='dénivelé positif cumulé (m)')),
                ('elevation_loss', models.FloatField(verbose_name='dénivelé négatif cumulé (m)')),
                ('duration', models.FloatField(verbose_name='durée estimée (h)')),
                ('difficulty', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='difficulté')),
            ],
        ),
    ]
