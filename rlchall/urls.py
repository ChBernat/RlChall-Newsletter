from django.conf.urls import patterns, include, url
from django.contrib import admin

import rlchall

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rlchall.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('newsletter.urls')),
)
