# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=11),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=11),
        ),
    ]