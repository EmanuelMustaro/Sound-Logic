# Generated by Django 3.2.15 on 2022-12-04 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0040_recentsearches_search_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentsearches',
            name='search_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 4, 19, 16, 35, 681299, tzinfo=utc)),
        ),
    ]
