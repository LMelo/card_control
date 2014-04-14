from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from views import index

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'sodexo/', include('sodexo.urls', namespace='sodexo')),
)
