# Generated by Django 5.1 on 2024-08-16 20:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0004_rename_user_touristplace_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristplace',
            name='description',
        ),
        migrations.RemoveField(
            model_name='touristplace',
            name='image',
        ),
        migrations.RemoveField(
            model_name='touristplace',
            name='location',
        ),
        migrations.RemoveField(
            model_name='touristplace',
            name='name',
        ),
        migrations.AddField(
            model_name='touristplace',
            name='city_tourist_map',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='touristplace',
            name='hotels',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='touristplace',
            name='languages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='touristplace',
            name='map_of_tourist_places_in_ecuador',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='touristplace',
            name='regions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='touristplace',
            name='traditional_music',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='touristplace',
            name='typical_food',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='touristplace',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='places', to=settings.AUTH_USER_MODEL),
        ),
    ]
