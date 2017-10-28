from django.conf.urls import url
from . import views

app_name = 'Gym'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^Trainee/add/$', views.TraineeCreate.as_view(), name='trainee-add'),
    url(r'^Trainee/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='trainee-detail'),
    url(r'^Trainee/(?P<pk>[0-9]+)/edit/$', views.TraineeUpdate.as_view(), name='trainee-update'),
    url(r'^Trainee/(?P<pk>[0-9]+)/delete/$', views.TraineeDelete.as_view(), name='trainee-delete'),
]
