# Generated by Django 4.1.1 on 2022-09-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_netflix_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netflix',
            name='movie',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
