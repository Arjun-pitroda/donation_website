# Generated by Django 3.1.2 on 2020-11-20 13:30

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0005_location_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]