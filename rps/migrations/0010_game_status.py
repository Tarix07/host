# Generated by Django 2.2.1 on 2019-05-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rps', '0009_auto_20190521_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.TextField(blank=True, default='waiting'),
        ),
    ]
