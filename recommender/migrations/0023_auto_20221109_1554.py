# Generated by Django 3.2.15 on 2022-11-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0022_auto_20221109_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_artist',
            field=models.ManyToManyField(blank=True, null=True, to='recommender.Artist'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_id',
            field=models.TextField(default='<function uuid4 at 0x0000010E1400F9A0>', editable=False, primary_key=True, serialize=False),
        ),
    ]
