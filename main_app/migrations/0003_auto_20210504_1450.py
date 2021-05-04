# Generated by Django 3.2 on 2021-05-04 09:50

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_mensservice_sharedservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MensService',
        ),
        migrations.DeleteModel(
            name='SharedService',
        ),
    ]