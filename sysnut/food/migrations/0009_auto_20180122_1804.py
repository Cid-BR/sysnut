# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-22 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_auto_20180122_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measure',
            name='food',
        ),
        migrations.AddField(
            model_name='food',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_measure', to='food.Measure', verbose_name='Medida'),
        ),
    ]