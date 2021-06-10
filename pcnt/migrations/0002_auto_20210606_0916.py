# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcnt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm_state',
            name='CPU_Cores',
            field=models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0445 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u043d\u044b\u0445 \u044f\u0434\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='vm_state',
            name='GPU_Count',
            field=models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442'),
        ),
        migrations.AlterField(
            model_name='vm_state',
            name='RAM_Count_GB',
            field=models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u043e\u0439 \u041e\u0417\u0423'),
        ),
    ]
