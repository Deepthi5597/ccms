# Generated by Django 3.0.6 on 2020-06-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/services')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='RecentImage',
            new_name='GalleryImage',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]