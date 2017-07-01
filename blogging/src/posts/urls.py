from django.conf.urls import url 
from posts.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView # post_list_view 

urlpatterns = [
    #url(r'^$', post_list_view, 'list'),
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete'),
    
]