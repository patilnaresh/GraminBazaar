from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Okos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^graminbazaar', 'graminbazaar.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
