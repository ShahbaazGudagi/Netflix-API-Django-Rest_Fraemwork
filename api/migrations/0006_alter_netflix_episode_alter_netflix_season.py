# Generated by Django 4.1.1 on 2022-09-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_netflix_movie_alter_netflix_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netflix',
            name='episode',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='season',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]