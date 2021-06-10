# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pcnt', '0011_auto_20210607_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vm_creation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='vm_state',
            name='name',
        ),
        migrations.AlterField(
            model_name='vm_creation',
            name='user',
            field=models.ForeignKey(default=1, verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vm_state',
            name='user',
            field=models.ForeignKey(default=1, verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b', to=settings.AUTH_USER_MODEL),
        ),
    ]
