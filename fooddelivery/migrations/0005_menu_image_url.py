# Generated by Django 3.1 on 2020-10-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddelivery', '0004_restaurant_food_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_url',
            field=models.URLField(default=True, max_length=500),
            preserve_default=False,
        ),
    ]
