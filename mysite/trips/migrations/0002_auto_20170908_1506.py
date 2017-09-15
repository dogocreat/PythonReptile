# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, default='dogocreat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='trip_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 8, 7, 6, 56, 239871, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
