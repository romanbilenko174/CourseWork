#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class vm_state(models.Model):
	status = models.CharField(u'Статус виртуальной машины', max_length=30, )
	created_at = models.DateTimeField(u'Дата запуска виртуальной машины')
	updated_at = models.DateTimeField(u'Дата последнего обновления состояния виртуальной машины')
	CPU_Cores = models.IntegerField(u'Количество используемых процессорных ядер')
        RAM_Count_GB = models.IntegerField(u'Количество используемой ОЗУ')
        GPU_Count = models.IntegerField(u'Количество использованных видеокарт')
	ip = models.CharField(u'IP-адрес виртуальной машины', max_length=15)
	os = models.CharField(u'Название ОС виртуальной машины', max_length=45)
	ping = models.BooleanField(u'Есть ли пинг до вируальной машины',default=False)
	user = models.ForeignKey(User,verbose_name=u'Создатель виртуальной машины',on_delete=models.CASCADE)
	def __str__(self):
		return self.status
	class Meta:
		verbose_name = "Состояние виртуальной машины"
		verbose_name_plural = "Состояния виртуальных машин"
class vm_creation(models.Model):
	status = models.CharField(u'Статус виртуальной машины', max_length=30, default="Launching")
        creation_date_time = models.DateTimeField(u'Дата запуска виртуальной машины',default=timezone.now)
        CPU_Cores = models.IntegerField(u'Количество используемых процессорных ядер')
        RAM_Count_GB = models.IntegerField(u'Количество используемой ОЗУ')
        GPU_Count = models.IntegerField(u'Количество использованных видеокарт')
	user = models.ForeignKey(User,verbose_name=u'Создатель виртуальной машины',on_delete=models.CASCADE)
        def __str__(self):
                return self.status
        class Meta:
                verbose_name = "Запущенная виртуальная машина"
                verbose_name_plural = "Запущенные виртуальные машины"

