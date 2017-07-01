from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse


from .mixins import FormUserNeededMixin, OwnerMixin
from .forms import PostModelForm
from .models import Post

# Create your views here.

# Create

class PostCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    #queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = "posts/create_view.html"
    success_url = "/post/" 
    login_url = "/admin/create"

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(PostCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You're not logged in"])
    #         return self.form_invalid(form)

    # def get_absolute_url(self):
    #     return reverse('post.views.details', args=[str(self.id)])




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

class PostUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = "posts/update_view.html"
    success_url = "/post/"

# Destroy

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    #template_name = "posts/delete_confirm.html" 
    # Por defecto busca una plantilla "app_confirm_delete.html", pero se le puede asignar un template_name
    success_url = reverse_lazy("home")

