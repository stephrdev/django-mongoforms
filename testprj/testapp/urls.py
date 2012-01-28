from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('testapp.views',
    url(r'^test001/$', 'test001', {}, 'test001'),
)
