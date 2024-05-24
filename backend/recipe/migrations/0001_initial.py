# Generated by Django 5.0.6 on 2024-05-24 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='NutritionalValueGeneric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.FloatField(verbose_name='Énergie (kcal)')),
                ('fat', models.FloatField(verbose_name='Matières grasses')),
                ('saturated_fat', models.FloatField(verbose_name='Acides gras saturés')),
                ('carbohydrates', models.FloatField(verbose_name='Glucides')),
                ('sugar', models.FloatField(verbose_name='Sucres')),
                ('protein', models.FloatField(verbose_name='Protéines')),
                ('salt', models.FloatField(verbose_name='Sel')),
                ('alcohol', models.FloatField(blank=True, null=True, verbose_name='Alcool')),
                ('fruits_vegetables_nuts', models.FloatField(verbose_name='Fruits, légumes, noix')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nom')),
                ('commercial_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nom commercial')),
                ('mk_code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code MK')),
                ('status', models.CharField(blank=True, max_length=200, null=True, verbose_name='Statut')),
                ('packaging_type', models.CharField(blank=True, choices=[('gd', 'Grand'), ('moy', 'Moyen'), ('pt', 'Petit')], max_length=4, null=True, verbose_name="Type d'emballage")),
                ('net_weight', models.FloatField(blank=True, null=True, verbose_name='Poids net')),
                ('ref_deli', models.CharField(blank=True, max_length=200, null=True, verbose_name='Référence DELI')),
                ('ref_ean', models.CharField(blank=True, max_length=200, null=True, verbose_name='Référence EAN')),
                ('ref_efl', models.CharField(blank=True, max_length=200, null=True, verbose_name='Référence EFL')),
                ('foodcost', models.FloatField(blank=True, null=True, verbose_name='Coût de la matière première')),
                ('packaging_price', models.FloatField(blank=True, null=True, verbose_name="Prix de l'emballage")),
                ('workcost', models.FloatField(blank=True, null=True, verbose_name="Coût de la main d'oeuvre")),
                ('profit_margin', models.FloatField(blank=True, null=True, verbose_name='Marge bénéficiaire')),
                ('selling_price', models.FloatField(blank=True, null=True, verbose_name='Prix de vente')),
                ('DLC', models.DateField(blank=True, null=True, verbose_name='Date limite de consommation')),
                ('technical_sheet', models.FileField(blank=True, null=True, upload_to='technical_sheets/', verbose_name='Fiche technique')),
                ('correction_ratio', models.FloatField(blank=True, null=True, verbose_name='Ratio de correction')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.category', verbose_name='Catégorie')),
            ],
        ),
        migrations.CreateModel(
            name='NutritionalValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.FloatField(verbose_name='Énergie (kcal)')),
                ('fat', models.FloatField(verbose_name='Matières grasses')),
                ('saturated_fat', models.FloatField(verbose_name='Acides gras saturés')),
                ('carbohydrates', models.FloatField(verbose_name='Glucides')),
                ('sugar', models.FloatField(verbose_name='Sucres')),
                ('protein', models.FloatField(verbose_name='Protéines')),
                ('salt', models.FloatField(verbose_name='Sel')),
                ('alcohol', models.FloatField(verbose_name='Alcool')),
                ('fruits_vegetables_nuts', models.FloatField(verbose_name='Fruits, légumes, noix')),
                ('ingredient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipe.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Titre')),
                ('is_ingredient', models.BooleanField(default=False, verbose_name='Ingrédient')),
                ('is_final', models.BooleanField(default=False, verbose_name='Produit fini')),
                ('ingredient', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_text', models.CharField(max_length=200)),
                ('step_number', models.IntegerField()),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(choices=[('kg', 'Kilogramme'), ('l', 'Litre')], max_length=4)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipe.recipe')),
            ],
        ),
    ]