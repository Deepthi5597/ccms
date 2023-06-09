# Generated by Django 3.0.2 on 2020-01-18 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sect', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('sect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.NewsType')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
