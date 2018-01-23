# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-23 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('weight', models.DecimalField(decimal_places=2, default=100.0, max_digits=8, verbose_name='Peso líquido (ml ou g)')),
                ('energy', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Energia (kcal)')),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Carboidratos (g)')),
                ('total_fat', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Gorduras Totais (g)')),
                ('poly_fat', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Gorduras Poli (g)')),
                ('mono_fat', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Gorduras Mono (g)')),
                ('sat_fat', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Gorduras Saturadas (g)')),
                ('protein', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Proteínas (g)')),
                ('total_fibers', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Fibras Totais (g)')),
                ('sol_fibers', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Fibras Solúveis (g)')),
                ('insol_fibers', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Fibras Insolúveis (g)')),
                ('cholesterol', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Colesterol (mg)')),
                ('retinol', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Retinol (Vit A) (mg)')),
                ('ac_ascorbic', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Ácido Ascórbico (Vit C) (mg)')),
                ('tiamine', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Tiamina (Vit B1) (mg)')),
                ('riboflavin', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Riboflavina (Vit B2) (mg)')),
                ('pyridoxine', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Piridoxina (Vit B6) (mg)')),
                ('cobalamin', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Cobalamina (Vit B12) (mcg)')),
                ('dvitamin', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Vitamina D (mcg)')),
                ('niacin', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Niacina (Vit B3)(mg)')),
                ('ac_folic', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Ácido fólico (Vit B9)(mcg)')),
                ('ac_pant', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Ácido pantotênico (Vit B5)(mg)')),
                ('tocopherol', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Tocoferol (Vit E)(mg)')),
                ('iodine', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Iodo (mcg)')),
                ('sodium', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Sódio (mg)')),
                ('calcium', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Cálcio (mg)')),
                ('magnesium', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Magnésio (mg)')),
                ('zinc', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Zinco (mg)')),
                ('manganese', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Manganês (mg)')),
                ('potassium', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Potássio (mg)')),
                ('phosphor', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Fósforo (mg)')),
                ('iron', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Ferro (mg)')),
                ('copper', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Cobre (mg)')),
                ('selenium', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Selênio (mcg)')),
            ],
            options={
                'verbose_name_plural': 'Alimentos',
                'verbose_name': 'Alimento',
            },
        ),
        migrations.CreateModel(
            name='MealItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(choices=[('CAFÉ DA MANHÃ', 'Café da Manhã'), ('LANCHE I', 'Lanche I'), ('ALMOÇO', 'Almoço'), ('LANCHE II', 'Lanche II'), ('JANTAR', 'Jantar'), ('CEIA', 'Ceia')], default=None, max_length=40, null=True, verbose_name='Refeição')),
                ('weight', models.DecimalField(decimal_places=2, default=100.0, max_digits=8, verbose_name='Quantidade')),
                ('food_analysis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal_analysis', to='patient.FoodAnalysis', verbose_name='Cardápio')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, default=100.0, max_digits=8, verbose_name='Unidade de Medida')),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measure_food', to='food.Food', verbose_name='Alimento')),
            ],
        ),
        migrations.CreateModel(
            name='MeasureUnity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, unique=True, verbose_name='Descrição da Medida')),
            ],
        ),
        migrations.CreateModel(
            name='SubstituteItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_substitute', models.DecimalField(decimal_places=2, default=100.0, max_digits=8, verbose_name='Quantidade')),
                ('food_analysis_substitute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_analysis', to='patient.FoodAnalysis', verbose_name='Cardápio')),
                ('food_substitute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_food', to='food.Food', verbose_name='Alimento')),
                ('meal_substitute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_meal', to='food.MealItem', verbose_name='Refeição')),
                ('unity_substitute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_unity', to='food.MeasureUnity', verbose_name='Unidade de Medida')),
            ],
        ),
        migrations.CreateModel(
            name='UploadSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição da Tabela')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('path', models.FileField(blank=True, null=True, upload_to='upload/table', verbose_name='Tabela')),
            ],
        ),
        migrations.AddField(
            model_name='measure',
            name='measure_unity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measure_unity', to='food.MeasureUnity', verbose_name='Unidade de Medida'),
        ),
        migrations.AddField(
            model_name='mealitem',
            name='measure_unity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal_unity', to='food.MeasureUnity', verbose_name='Unidade de Medida'),
        ),
        migrations.AddField(
            model_name='mealitem',
            name='original_food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal_food', to='food.Food', verbose_name='Alimento'),
        ),
    ]
