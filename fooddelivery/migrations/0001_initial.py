# Generated by Django 3.1.2 on 2021-06-20 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_version', models.CharField(max_length=200)),
                ('other_details', models.CharField(max_length=200)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('item_description', models.CharField(max_length=150)),
                ('item_price', models.DecimalField(decimal_places=5, max_digits=50)),
                ('other_details', models.CharField(max_length=150)),
                ('image_url', models.URLField(max_length=500)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fooddelivery.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_address', models.CharField(max_length=200)),
                ('staff_contact', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('restaurant_address', models.CharField(max_length=150)),
                ('restaurant_contact', models.CharField(max_length=150)),
                ('food_description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=False, max_length=200)),
                ('address', models.CharField(default=False, max_length=200)),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=5, max_digits=50)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('customers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fooddelivery.customer')),
                ('menuitem', models.ManyToManyField(to='fooddelivery.MenuItem')),
            ],
        ),
    ]
