from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^FAQ/', include('FAQ.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


