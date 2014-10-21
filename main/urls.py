__author__ = 'Stepan'

from django.conf.urls import patterns, url
from main import views
from fsblog import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^tours', views.tours, name='tours'),
    url(r'^author', views.author, name='author'),
    url(r'^sign-up-for-a-tour', views.signUpForATour, name='sign-up-for-a-tour'),
    url(r'^articles', views.articles, name='articles'),
    url(r'^article/(\d+)', views.article, name='article'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)