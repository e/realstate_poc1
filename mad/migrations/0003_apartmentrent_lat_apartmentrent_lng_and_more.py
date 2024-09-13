# Generated by Django 5.1.1 on 2024-09-13 12:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mad', '0002_remove_advert_title_advert_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentrent',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentrent',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='apartmentsale',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentsale',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentsale',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='room',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]