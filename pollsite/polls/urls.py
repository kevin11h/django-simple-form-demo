from django.conf.urls.defaults import *

urlpatterns = patterns('polls.views',
    (r'^$', 'index'),
    (r'^(\d+)/$', 'detail'),
    (r'^(\d+)/vote/$', 'vote'),
    (r'^(\d+)/results/$', 'results'),
)