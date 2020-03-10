from django.shortcuts import render
from .models import PostItems
# Create your views here.


def index(request):
    context = {
        'posts': PostItems.objects.all()
    }
    return render(request, 'blog/index.html', context)


    