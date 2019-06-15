# Generated by Django 2.2.2 on 2019-06-12 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_eventcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcomments',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_event', to='dates.Event'),
        ),
        migrations.AlterField(
            model_name='eventcomments',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
