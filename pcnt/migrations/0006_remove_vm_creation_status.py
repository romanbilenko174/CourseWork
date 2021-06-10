# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcnt', '0005_vm_creation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vm_creation',
            name='status',
        ),
    ]
