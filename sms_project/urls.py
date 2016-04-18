from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sms_project.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sms_app/', include('sms_app.urls', namespace = 'sms_app')),
)
