# Generated by Django 3.1.2 on 2020-11-07 16:46

from django.db import migrations, models
import django.db.models.deletion
import donation.models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to=donation.models.user_directory_path)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_post', to='donation.post')),
            ],
        ),
    ]
