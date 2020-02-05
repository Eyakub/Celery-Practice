from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    url(r'^$', views.UsersListView.as_view(), name='users_list'),
    url(r'^generate/$', views.GenerateRandomUserView.as_view(), name='generate'),

]
