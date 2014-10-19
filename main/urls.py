__author__ = 'Stepan'

from django.conf.urls import patterns, url
from main import views
from fsblog import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^tours', views.tours, name='tours'),
    url(r'^sign-up-for-a-tour', views.signUpForATour, name='sign-up-for-a-tour'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)