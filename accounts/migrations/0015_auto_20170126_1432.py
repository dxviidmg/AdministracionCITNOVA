# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-26 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20170126_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Tecnico', 'Tecnico'), ('Ing.', 'Ing.'), ('Dr.', 'Dr.'), ('Mtro(a).', 'Mtro(a).'), ('Lic.', 'Lic.'), ('T. S. U.', 'T. S. U.')], max_length=30, null=True),
        ),
    ]
