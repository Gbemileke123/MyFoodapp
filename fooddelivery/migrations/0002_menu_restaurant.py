# Generated by Django 3.1.2 on 2021-06-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fooddelivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fooddelivery.restaurant'),
        ),
    ]
