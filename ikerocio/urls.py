from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ikerocio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ikerocio.views.home', name='home'),
    url(r'^check-form/', 'ikerocio.views.check_form', name='check-form'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^cv/', include('cv.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
    #url(r'^cv/', include('cv.urls')),
)
urlpatterns += staticfiles_urlpatterns()