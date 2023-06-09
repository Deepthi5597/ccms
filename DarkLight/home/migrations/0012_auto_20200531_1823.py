# Generated by Django 3.0.6 on 2020-05-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200531_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.CharField(choices=[('fa fa-facebook', 'Facebook'), ('fa fa-twitter', 'Twitter'), ('fa fa-linkedin', 'LinkedIn'), ('fa fa-pintrest', 'Pintrest'), ('fa fa-snapchat', 'Snapchat'), ('fa fa-youtube', 'Youtube'), ('fa fa-reddit-alien', 'Reddit'), ('fa fa-medium', 'Medium'), ('fa fa-google-plus', 'Google Plus'), ('fa fa-js-fiddle', 'Fiddle'), ('fa fa-github', 'Github')], default='fa fa-facebook', max_length=120),
        ),
    ]
