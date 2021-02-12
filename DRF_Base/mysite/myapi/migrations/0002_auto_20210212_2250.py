# Generated by Django 3.1.6 on 2021-02-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='pics')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
