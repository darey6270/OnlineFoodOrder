# Generated by Django 4.0.4 on 2022-04-27 18:16

import FoodOrdering.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodOrdering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=FoodOrdering.models.food_image),
        ),
    ]
