# Generated by Django 5.0.2 on 2024-03-29 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_adventurepackage_accommodation_price_per_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adventurepackage',
            name='food_and_accommodation_price_per_person',
        ),
    ]
