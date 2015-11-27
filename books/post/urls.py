from django.conf.urls import patterns, url

from post import views

urlpatterns = patterns(
    '',
    url(r'^$', views.PostListView.as_view(), name='posts'),
    url(r'^add/$', views.PostCreateView.as_view(), name='add_post'),
    url(r'^edit/(?P<pk>\d+)/$', views.PostEditView.as_view(), name='edit_post'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(pk_url_kwarg='pk'), name='view'),
    url(r'^delpost/(?P<pk>\d+)/$', views.PostDeleteView.as_view(), name='delete_post'),
    url(r'^addcomment/(?P<post_pk>\d+)/$', views.CommentCreateView.as_view(pk_url_kwarg='post_pk'), name='add_comment'),
    url(r'^delcomment/(?P<post_pk>\d+)/$', views.CommentDeleteView.as_view(pk_url_kwarg='post_pk'), name='delete_comment'),
    
    
    url(r'^logout/$', views.PostListView.as_view(), name='logout'),
#    url(r'^add/comment/(?P<post_pk>\d+)/$',
#        views.CommentCreateView.as_view(), name='add_comment'),
)
