from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.posts', name='home-blog'),
                       url(r'^page/(?P<page>\d+)/$', 'blog.views.posts', ),
                       url(r'^tag/(?P<tag>\S+)/$', 'blog.views.posts', name='tag_detail'),
                       url(r'^category/(?P<category>\S+)/$', 'blog.views.posts', name='category_detail'),
                       # url(r'^p/$', views.BlogIndex.as_view(), name='index' ),
                       url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name='entry_detail'),
)
