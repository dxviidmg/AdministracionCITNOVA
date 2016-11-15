# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlPresupuestal', '0012_partida_monto_enero_ejercido'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='monto_abril_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_agosto_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_diciembre_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_febrero_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_julio_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_junio_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_marzo_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_mayo_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_noviembre_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_octubre_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_septiembre_ejercido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
