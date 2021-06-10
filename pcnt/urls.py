from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'controller.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'pcnt.views.index'),
    url(r'^vm/', 'pcnt.views.vm'),
    url(r'^pcocc/', 'pcnt.views.pcocc'),
    url(r'^spice/', 'pcnt.views.spice'),
    url(r'^tpl$', 'pcnt.views.template_list'),
    url(r'^login$', 'pcnt.views.login_view'),
    url(r'^logout$', 'pcnt.views.logout_view'),
]


