# Generated by Django 2.2.6 on 2020-01-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0004_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
