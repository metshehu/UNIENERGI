# Generated by Django 5.1.3 on 2024-11-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensorName', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=5)),
                ('timestamp', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
