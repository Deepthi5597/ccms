# Generated by Django 3.0.6 on 2020-05-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_slider_first'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/portfolio')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='slider',
            name='desc',
        ),
    ]
