# Generated by Django 5.0.2 on 2024-03-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_yourresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventurepackage',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]