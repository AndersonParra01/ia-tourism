# Generated by Django 5.1 on 2024-08-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0012_rename_destination_tourist_touristplace_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristplace',
            name='especific_destination',
            field=models.TextField(blank=True, null=True),
        ),
    ]
