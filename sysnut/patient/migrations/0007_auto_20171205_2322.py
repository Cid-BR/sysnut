# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 02:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20171205_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guidanceaux',
            old_name='description',
            new_name='description2',
        ),
    ]