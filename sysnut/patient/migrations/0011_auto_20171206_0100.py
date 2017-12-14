# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_auto_20171206_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidance',
            name='show',
        ),
        migrations.RemoveField(
            model_name='guidanceaux',
            name='show',
        ),
        migrations.AlterField(
            model_name='foodanalysis',
            name='guidanceaux',
            field=models.ManyToManyField(related_name='analysis_guidanceaux', to='patient.GuidanceAux', verbose_name='Orientação'),
        ),
    ]