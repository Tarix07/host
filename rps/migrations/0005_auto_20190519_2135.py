# Generated by Django 2.2.1 on 2019-05-19 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rps', '0004_game_game_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='creator_choice',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='opponent_choice',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
