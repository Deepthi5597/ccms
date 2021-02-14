# Generated by Django 3.0.6 on 2020-06-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=70)),
                ('company', models.CharField(max_length=70)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonial_images')),
            ],
        ),
    ]