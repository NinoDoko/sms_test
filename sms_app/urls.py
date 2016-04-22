from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^sms_template/$', views.sms_template_index, name = 'sms_template_index'),
    url(r'^sms_template_history/$', views.sms_history, name = 'sms_template_history'),
    url(r'^sms_template/(\d+)$', views.view_sms_template, name = 'view_sms_template'),
    url(r'^send_sms/(\d+)$', views.send_sms, name = 'send_sms'),
    url(r'^delete_sms_template/(\d+)$', views.delete_sms_template, name = 'delete_sms_template'),
    url(r'^log_out$', views.log_out, name = 'logout'),
)
