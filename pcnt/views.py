#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.http import HttpResponse
from .models import vm_creation
from .forms import vm_creationForm, vm_state
from datetime import datetime
from django.db import models
from django.utils.timezone import now
from .functions import getNodeStates, getJobStates, getPCOCCImageList,pcocc_import_image, pcocc_remove_image, get_templates, pcocc_show
from django.core.files.storage import FileSystemStorage


def index(request):
	error = ''
	username = None
    	if request.user.is_authenticated():
        	username = request.user
	form = vm_creationForm({'user':username})
	if request.method == 'POST':
		if request.POST.get("send_form"):
			form = vm_creationForm(request.POST)
			if form.is_valid():
				data=form.save(commit=False)
				data.user=username
				data.save()
				redirect('/vm')
			else:
				error = 'Форма была неверной'
	context={
		'form':form,
		'error':error,
		'getNodeStates':getNodeStates,
		'getJobStates':getJobStates,
		}
	return render(request, 'index.html',context)
def vm(request):
        v_state = vm_state.objects.filter(user=request.user)
        return render(request, 'vm.html',{'vm_state':v_state})
def pcocc(request):
	username = None
	template_name = ""
	pcocc_sh = []
        if request.user.is_authenticated():
                username = request.user.username
	if username == "admin":
		username = "root"
	pcocc_images = getPCOCCImageList(username)	 
	pcocc_templates = get_templates(username)
	context={
			'getPCOCCImageList':pcocc_images,
			'get_templates':pcocc_templates,
                }
	if request.method == 'POST' and request.POST.get('show_templates_data'):
                template_name = request.POST.get('show_templates_data')
                pcocc_sh = pcocc_show(username,template_name)
		cintext['pcocc_sh']= pcocc_sh
	if request.method == 'POST' and request.POST.get('template_remove_name'):
		template_name = request.POST.get('template_remove_name')
		pcocc_remove = pcocc_remove_image(username,template_name)
#       if request.method == 'POST' and request.FILES['myfile']:
#               myfile = request.FILES['myfile']
#               path = "/home/"+username+"/pcocc_media/"+myfile.name
#               fs = FileSystemStorage(location=path)
#               filename = fs.save(myfile.name, myfile)
#               name = "test"
#               pcocc_imp = pcocc_import_image(username,path,name)
	return render(request, 'pcocc.html',context) 
def spice(request):
	return render(request, 'spice.html')
def template_list(request):
	return render(request, 'template_list.html')
def login_view(request):
	if request.user.is_authenticated():
       		 return HttpResponseRedirect('/')
	else:
       	    if request.POST:
            	username = request.POST.get('login')
            	password = request.POST.get('password')
            	if username.lower() not in ['root', 'admin', 'administrator', 'user']:
                	user = authenticate(username=username, password=password)
           	else:
                	user = None
            	if user is not None:
                	if user.is_active:
                    		login(request, user)
                    		return HttpResponseRedirect('/')
                	else:
                   		return render(request, 'login.html', {'user': request.user, 'message': u'Пользователь отключен'})
            	else:
                	return render(request, 'login.html', {'user': request.user, 'message': u'Ошибка авторизации'}, status=401)
            else:
           	return render(request, 'login.html', {'user': request.user})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
