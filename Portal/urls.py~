from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import Portal.views

urlpatterns = [
    # Examples:
    url(r'^$', 'Portal.views.home', name='home'),
    url(r'^register/$', 'Portal.views.register', name='register'),
    url(r'^reg/$', 'Portal.views.reg', name='reg'),
    url(r'^reg_goo/$', 'Portal.views.reg_goo', name='reg_goo'),
    url(r'^goo/$', 'Portal.views.goo', name='goo'),
    url(r'^jseek/$', 'Portal.views.jseek', name='jseek'),
    url(r'^rec/$', 'Portal.views.rec', name='rec'),
    url(r'^rauth/$', 'Portal.views.rauth', name='rauth'),
    url(r'^jauth/$', 'Portal.views.jauth', name='jauth'),
    url(r'^logout/$', 'Portal.views.logout', name='logout'),
    url(r'^r_login/$', 'Portal.views.r_login', name='r_login'),
    url(r'^rcheck/$', 'Portal.views.rcheck', name='rcheck'),
    url(r'^save/$', 'Portal.views.save', name='save'),
    url(r'^entry/$', 'Portal.views.entry', name='entry'),
    url(r'^mark/$', 'Portal.views.mark', name='mark'),
    url(r'^report/$', 'Portal.views.report', name='report'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
]
