from django.conf.urls import patterns, url
#from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('rems.views',
    url(r'^$', 'report_list', name='report_list'),
    url(r'^(?P<pk>\d+)/$', 'report_detail', name='report_detail'),
)

# Format suffixes
#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
