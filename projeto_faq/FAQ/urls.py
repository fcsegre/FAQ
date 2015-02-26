from django.conf.urls import patterns, url

from FAQ import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
