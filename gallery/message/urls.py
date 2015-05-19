from django.conf.urls import patterns, url

from message import views

urlpatterns = patterns('',

    # ex: /page/about/
    # url(r'^$', views.albums, name='albums'),
    url(r'^add/$', views.add_msg, name='add_msg'),
    url(r'^show/(?P<mid>\S+)/$', views.show_msg, name='show_msg'),
)