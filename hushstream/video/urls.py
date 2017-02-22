from django.conf.urls import url
import django.contrib.auth.views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/', django.contrib.auth.views.login, name='login'),
    url(r'^video/', views.video, name='video'),
    url(r'^logout/', views.logout, name='logout'),
]
