from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = patterns('',
	url(r'^$', views.homepage, name='homepage'),
	url(r'^newsletter/$', views.newsletter, name='newsletter'),
    url(r'^panel/news-manager/$', views.manage_news, name='news-manager'),
    url(r'^panel/mails-manager/$', views.manage_mails, name='mails-manager'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^logging-failure/$', views.failure, name='logging-failure'),
    (r'^login/$',  login),
    (r'^logged-out/$', logout),
	)