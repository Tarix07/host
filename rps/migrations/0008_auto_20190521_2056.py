# Generated by Django 2.2.1 on 2019-05-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rps', '0007_auto_20190521_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_name',
            field=models.TextField(blank=True, max_length=50, unique=True),
        ),
    ]
