# Generated by Django 3.1 on 2020-09-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddelivery', '0003_auto_20200919_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='food_description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
