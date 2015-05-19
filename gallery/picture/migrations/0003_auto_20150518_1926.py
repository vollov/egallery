# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picture.models
import picture.storage


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_auto_20150412_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=picture.storage.OverwriteStorage(), upload_to=picture.models.image_upload_path),
        ),
    ]
