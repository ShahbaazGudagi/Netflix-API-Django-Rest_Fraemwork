# Generated by Django 4.1.1 on 2022-09-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_netflix_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netflix',
            name='movie',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='series',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
