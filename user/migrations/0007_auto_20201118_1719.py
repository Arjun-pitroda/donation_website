# Generated by Django 3.1.2 on 2020-11-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Feeling Great', max_length=300, null=True),
        ),
    ]