from django.contrib import admin
from django.contrib.auth.models import Group
from .models import vm_state, vm_creation
# Register your models here.

admin.site.register(vm_state)
admin.site.register(vm_creation)
admin.site.unregister(Group)
