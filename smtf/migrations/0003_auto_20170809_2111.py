# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smtf', '0002_auto_20170621_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smtfparticipant',
            name='preferredCity',
            field=models.CharField(choices=[('Goa', 'Goa'), ('Bangalore', 'Bangalore'), ('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Delhi', 'Delhi'), ('Vizag', 'Vizag'), ('Ahmedabad', 'Ahmedabad'), ('Chennai', 'Chennai'), ('Hyderabad', 'Hyderabad')], max_length=20),
        ),
    ]
