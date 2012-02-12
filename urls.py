from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Index page
    (r'^polls/$', 'polls.views.index'),

    # Poll page
    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),

    # Poll results page
    (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.result'),

    # Poll voting page
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

)
