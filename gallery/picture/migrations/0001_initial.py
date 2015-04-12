# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picture.models
import picture.storage
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=60)),
                ('public', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, null=True, blank=True)),
                ('image_key', models.CharField(default=uuid.uuid4, max_length=64, verbose_name='Activation key')),
                ('image', models.ImageField(storage=picture.storage.OverwriteStorage(), upload_to=picture.models.image_upload_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(to='picture.Album')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
