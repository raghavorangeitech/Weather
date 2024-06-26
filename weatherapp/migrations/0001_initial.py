# Generated by Django 5.0.4 on 2024-04-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precipitation', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
