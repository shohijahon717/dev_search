# Generated by Django 3.2.9 on 2021-12-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
