# Generated by Django 3.2.9 on 2021-12-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_recipiend_message_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
