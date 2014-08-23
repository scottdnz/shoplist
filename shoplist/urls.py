from django.conf.urls import patterns, include, url

from interface.views.ingredients import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shoplist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^ingredients/$', index),

    url(r'^admin/', include(admin.site.urls)),
)
