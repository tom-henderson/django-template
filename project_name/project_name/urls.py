from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.log_out, name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
)
