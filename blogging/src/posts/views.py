from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.

# Create

# Retrieve

class PostDetailView(DetailView):
    queryset = Post.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     return Post.objects.get(id=1)

class PostListView(ListView):
    queryset = Post.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        return context

# def post_list_view(request):
#     queryset = Post.object.all()
#     for obj in queryset:
#         print(obj.title)
#     context = {
#         "object_list": queryset
#     }

#     return render(request, "posts/post_list.html", context)

# Update

# Destroy