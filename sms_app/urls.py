from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^sms_template/$', views.sms_template_index, name = 'sms_template_index'),
    url(r'^template_action/(\d+)$', views.sms_action, name = 'sms_template_action'),
    url(r'^sms_template_history/$', views.sms_history, name = 'sms_template_history'),
    url(r'^sms_template_stats/(\d+)$', views.sms_stats, name = 'sms_template_stats'),
    url(r'^sms_template/(\d+)$', views.view_sms_template, name = 'view_sms_template'),
    url(r'^delete_sms_template/(\d+)$', views.delete_sms_template, name = 'delete_sms_template'),
    
    url(r'^manage_users/$', views.manage_users, name = 'manage_users'),
    
    url(r'^template_schedule/(\d+)/remove(\d+)$', views.unschedule_template, name = 'unschedule_template'),
    
    url(r'^manage_auto_reply/add/(\d+)$', views.add_auto_reply, name = 'add_auto_reply'),
    url(r'^manage_auto_reply/remove/(\d+)$', views.remove_auto_reply, name = 'remove_auto_reply'),
    url(r'^manage_auto_reply/subscribe_users/(\d+)$', views.subscribe_users, name = 'subscribe_users'),
    
    url(r'^sms_tools_log/$', views.sms_tools_log, name = 'sms_tools_log'),
    url(r'^send_sms/(\d+)$', views.send_sms, name = 'send_sms'),

    url(r'^log_out$', views.log_out, name = 'logout'),
)
