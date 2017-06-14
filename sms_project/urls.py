from django.conf.urls import include, url
from django.contrib import admin

import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sms_app/', include('sms_app.urls', namespace = 'sms_app')),
]
