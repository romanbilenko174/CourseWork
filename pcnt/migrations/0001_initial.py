# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vm_state',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=30, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b')),
                ('created_at', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b')),
                ('updated_at', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b')),
                ('CPU_Cores', models.IntegerField(max_length=6, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0445 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u043d\u044b\u0445 \u044f\u0434\u0435\u0440')),
                ('RAM_Count_GB', models.IntegerField(max_length=6, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u043e\u0439 \u041e\u0417\u0423')),
                ('GPU_Count', models.IntegerField(max_length=6, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442')),
                ('ip', models.CharField(max_length=15, verbose_name='IP-\u0430\u0434\u0440\u0435\u0441 \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b')),
                ('os', models.CharField(max_length=45, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u041e\u0421 \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b')),
                ('ping', models.BooleanField(default=False, verbose_name='\u0415\u0441\u0442\u044c \u043b\u0438 \u043f\u0438\u043d\u0433 \u0434\u043e \u0432\u0438\u0440\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b')),
            ],
        ),
    ]
