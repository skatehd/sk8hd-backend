# Generated by Django 2.2.2 on 2019-06-23 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shredmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
