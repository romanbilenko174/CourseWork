# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pcnt', '0003_auto_20210606_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='vm_creation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b')),
                ('CPU_Cores', models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0445 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u043d\u044b\u0445 \u044f\u0434\u0435\u0440')),
                ('RAM_Count_GB', models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u043e\u0439 \u041e\u0417\u0423')),
                ('GPU_Count', models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442')),
                ('user', models.ForeignKey(default=1, verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043f\u0443\u0449\u0435\u043d\u043d\u0430\u044f \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u0430\u044f \u043c\u0430\u0448\u0438\u043d\u0430',
                'verbose_name_plural': '\u0417\u0430\u043f\u0443\u0449\u0435\u043d\u043d\u044b\u0435 \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435 \u043c\u0430\u0448\u0438\u043d\u044b',
            },
        ),
        migrations.AddField(
            model_name='vm_state',
            name='user',
            field=models.ForeignKey(default=1, verbose_name='\u0421\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u044c \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u0430\u0448\u0438\u043d\u044b', to=settings.AUTH_USER_MODEL),
        ),
    ]
