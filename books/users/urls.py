from django.conf.urls import patterns, url

from users import views
from django.contrib.auth import views as auth_views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.UserCreateView.as_view(), name='create_user'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'), 
    url(r'^list/$', views.UserList.as_view(), name='userlist'),    
   )
   
   
   
   
   
    
'''
    url(r'^password/reset$', auth_views.password_reset, 
    {'template_name': 'form.html', 'post_reset_redirect': '/'}, 
    name='password_reset'),
    
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/' 
    r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.password_reset_confirm,
    {'template_name': 'password_reset_confirm.html'},
    name='password_reset_confirm'),
    
    url(r'^password/reset/complete$',
    auth_views.password_reset_complete,
    {'template_name': 'password_reset_complete.html'},
    name='password_reset_complete')
'''
