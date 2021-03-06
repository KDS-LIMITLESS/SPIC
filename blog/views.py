from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import PostItems
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {
        'posts': PostItems.objects.all()
    }
    return render(request, 'blog/index.html', context)

class PostListView(ListView):
    model = PostItems
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = PostItems
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    paginate_by = 3  

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostItems.objects.filter(author=user).order_by('-date_posted')

    
class Post_Detail(DetailView):
    model = PostItems

class CreatePost(LoginRequiredMixin, CreateView):
    model = PostItems
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostItems
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

 
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostItems
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
