from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import *
from django.views.generic import ListView,DetailView,View
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect

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
    

class PostDetails(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post':post,
            'comment_form':CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'tag':post.tags.all(),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request,'blog/post-details.html',context)
    def post(self, request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("postimi", args=[slug]))
        
        
        context = {
            'post':post,
            'comment_form':CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'tag':post.tags.all(),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request,'blog/post-details.html',context)

class ReadLater(View):

    def get(self,request):
        stored_post = request.session.get("stored_posts")

        context = {}

        if stored_post is None or len(stored_post)==0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in= stored_post)
            context["posts"] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored-post.html', context)
    
    
    
    def post(slef,request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session['stored_posts'] = stored_posts
        
        return HttpResponseRedirect('/')

