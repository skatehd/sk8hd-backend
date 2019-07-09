# Generated by Django 2.2.2 on 2019-06-23 14:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shredmap', '0002_location_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tricks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('trick', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trick_location', to='shredmap.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_trick_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocationComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_location', to='shredmap.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_comment_owner', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shredmap.LocationComments')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_location', to='shredmap.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_image_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]