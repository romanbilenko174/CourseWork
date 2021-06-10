# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcnt', '0004_auto_20210606_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm_creation',
            name='status',
            field=models.CharField(default=b'Disabled', max_length=30, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b'),
        ),
    ]
