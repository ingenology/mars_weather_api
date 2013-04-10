from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('rems.views',
    url(r'^$', 'report_root', name='report_root'),
    url(r'^latest/$', 'report_latest', name='report_latest'),
    url(r'^archive/$', 'report_list', name='report_list'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
