# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-23 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20180121_1105'),
        ('food', '0011_auto_20180122_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='substituteitem',
            old_name='weight',
            new_name='weight_substitute',
        ),
        migrations.RemoveField(
            model_name='substituteitem',
            name='home_measure',
        ),
        migrations.RemoveField(
            model_name='substituteitem',
            name='mealitem',
        ),
        migrations.AddField(
            model_name='substituteitem',
            name='food_analysis_substitute',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_analysis', to='patient.FoodAnalysis', verbose_name='Cardápio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='substituteitem',
            name='meal_substitute',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_meal', to='food.MealItem', verbose_name='Refeição'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='substituteitem',
            name='unity_substitute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_unity', to='food.MeasureUnity', verbose_name='Unidade de Medida'),
        ),
        migrations.AlterField(
            model_name='substituteitem',
            name='food_substitute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_food', to='food.Food', verbose_name='Alimento'),
        ),
    ]