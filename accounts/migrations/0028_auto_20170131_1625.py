# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20170127_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='grado_profesional',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr.'), ('T. S. U.', 'T. S. U.'), ('Tecnico', 'Tecnico'), ('Lic.', 'Lic.'), ('Ing.', 'Ing.'), ('Mtro(a).', 'Mtro(a).')], max_length=30, null=True),
        ),
    ]
