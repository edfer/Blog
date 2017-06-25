from django.conf.urls import url 
from posts.views import PostDetailView, PostListView # post_list_view 

urlpatterns = [
    #url(r'^$', post_list_view, 'list'),
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
]