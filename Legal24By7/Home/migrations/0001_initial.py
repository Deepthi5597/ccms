# Generated by Django 3.0.6 on 2020-05-15 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=500)),
                ('documents', models.FileField(upload_to='credentials/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=120)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('details', models.CharField(max_length=500)),
                ('cost', models.IntegerField()),
                ('tag', models.CharField(max_length=120, null=True)),
                ('type', models.ManyToManyField(to='Home.Type')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('details', models.CharField(max_length=500)),
                ('documents', models.FileField(upload_to='credentials/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('lawyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.Lawyer')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.Service')),
            ],
        ),
    ]
