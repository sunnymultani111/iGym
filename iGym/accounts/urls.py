from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
     url(r'^/$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': 'accounts:login'}, name='logout'),
    url(r'^password/$', views.change_password, name='change_password'),
]
