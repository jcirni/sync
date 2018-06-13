from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^participants/$', views.participants, name='participants'),
    url(r'^participants/new/$', views.new_participant, name='new'),
    url(r'^participants/(?P<participant_id>[0-9]+)/status/(?P<participant_status>.*)/$', views.new_participant_status, name='new_status'),

]
