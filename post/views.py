from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import *
from django.views.generic import ListView,DetailView
# Create your views here.

"""
def starting_page(request): #faqa kryesore e blog
    latest_post = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {"posts":latest_post})
"""
def get_date(post):
    return post['date']

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        query_set= super().get_queryset()
        data = query_set[:3]
        return data

class AllPosts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = 'posts'
    ordering = ['-date']
    

class PostDetails(DetailView):
    template_name = "blog/post-details.html"
    model = Post

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['posts_tags'] = self.object.tags.all()
      return context
