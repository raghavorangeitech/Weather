# Generated by Django 5.0.4 on 2024-04-15 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WeatherData',
        ),
    ]