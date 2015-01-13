from django.conf.urls import patterns, include, url
from django.contrib import admin

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wtc_br.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.fetch_random_message),
    url(r'^(?P<id>\w+)/$', views.fetch_message),
)
