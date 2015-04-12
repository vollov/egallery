from django.conf.urls import patterns, url

from picture import views

urlpatterns = patterns('',

    # ex: /page/about/
    url(r'^$', views.albums, name='albums'),
    url(r'^album/(?P<title>\S+)/$', views.album, name='album'),
)