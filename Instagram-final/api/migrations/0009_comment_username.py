# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
