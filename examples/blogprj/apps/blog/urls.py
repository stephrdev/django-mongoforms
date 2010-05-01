# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to, direct_to_template

entry_pattern = patterns('apps.blog.views',
    (r'^$', 'show'),
    (r'^edit/$', 'edit'),
    (r'^delete/$', 'delete'),
)

urlpatterns = patterns('apps.blog.views',
    (r'^$', 'index'),
    (r'^new/$', 'new'),
    (r'^(?P<slug>[\w\-]+)/', include(entry_pattern)),
)