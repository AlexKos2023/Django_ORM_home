# Generated by Django 4.2.7 on 2024-02-11 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_car_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='client',
        ),
    ]
