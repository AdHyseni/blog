from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import *

# Create your views here.


def get_date(post):
    return post['date']

def starting_page(request): #faqa kryesore e blog
    latest_post = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {"posts":latest_post})

def posts(request): #faqa me listen e blogjeve
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html",{"posts":all_posts})

def post_details(request,slug):#faqa me artikullin e blog
    #identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-details.html",{'post':identified_post})