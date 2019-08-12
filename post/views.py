from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from post.models import Post


class ListPost(ListView):
    model = Post
    template_name = ''
    context_object_name = 'posts'
    queryset = Post.objects.all()
