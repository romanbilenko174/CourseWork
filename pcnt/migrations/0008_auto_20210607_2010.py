# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcnt', '0007_vm_creation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm_creation',
            name='user',
            field=models.CharField(default=1, max_length=30, verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='vm_state',
            name='user',
            field=models.CharField(default=1, max_length=30, verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b'),
        ),
    ]
