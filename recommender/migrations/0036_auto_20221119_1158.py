# Generated by Django 3.2.15 on 2022-11-19 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0035_album_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artist_tracks',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]