from django.shortcuts import render
from .models import PostItems
from django.views.generic import ListView, DetailView
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
    
class Post_Detail(DetailView):
    model = PostItems