# Generated by Django 3.0.6 on 2020-05-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200531_1823'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AlterField(
            model_name='recentimage',
            name='image',
            field=models.ImageField(upload_to='images/recent'),
        ),
    ]
