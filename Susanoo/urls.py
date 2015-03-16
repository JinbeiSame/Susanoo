from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Susanoo.app.views import *  

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'Susanoo.app.Home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'home/', Home.as_view()),
    url(r'tool/', Tool.as_view()),
    
)

urlpatterns += staticfiles_urlpatterns()