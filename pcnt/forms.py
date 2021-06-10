#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .models import vm_state, vm_creation
from django.forms import Form, ModelForm, NumberInput, TextInput,DateTimeField
from django.utils.timezone import now
class vm_creationForm(ModelForm):		
	class Meta:
        	model = vm_creation
		fields = ["CPU_Cores","RAM_Count_GB","GPU_Count"]
		widgets = {
                        "CPU_Cores":TextInput(attrs={
                                'min':'1',
				'max':'12',
				'type':'number',
				'style':'width:12ch',
                        }),
                        "RAM_Count_GB":TextInput(attrs={
                                'min':'1',
                                'max':'192',
                                'type':'number',
				'style':'width:12ch',
                        }),
			"GPU_Count":TextInput(attrs={
                                'min':'1',
                                'max':'4',
                                'type':'number',
				'style':'width:12ch',
                        }),
		}
