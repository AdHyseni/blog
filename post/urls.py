from django.urls import path

from . import views # nga folderi i blog importo file view

urlpatterns = [
    #path("", views.starting_page, name='faqa_kryesore'),
    path("",views.StartingPageView.as_view(), name='faqa_kryesore'),
    #path("post/", views.posts,name='postimet'),
    path("post/", views.AllPosts.as_view(),name='postimet'),
    #path("post/<slug:slug>", views.post_details, name='postimi'),
    path("post/<slug:slug>", views.PostDetails.as_view(), name='postimi'),

]
