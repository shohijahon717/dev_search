# Generated by Django 3.2.9 on 2021-12-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recipiend',
            new_name='recipient',
        ),
    ]
