# Generated by Django 3.1.6 on 2021-02-12 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20210212_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meme',
            old_name='author',
            new_name='credit',
        ),
    ]
