# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-26 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20170126_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('T. S. U.', 'T. S. U.'), ('Tecnico', 'Tecnico'), ('Dr.', 'Dr.'), ('Ing.', 'Ing.'), ('Mtro(a).', 'Mtro(a).'), ('Lic.', 'Lic.')], max_length=30, null=True),
        ),
    ]
