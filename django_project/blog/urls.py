from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('aboutus/', views.about, name="blog-about"),
    path('intro/', views.intro, name="blog-intro"),
    path('apply/', views.apply, name="blog-apply"),
    path('faq/', views.faq, name="blog-faq"),
    path('game/', views.game, name="game"),
    path('form_econ/', views.formEcon, name="form-econ"),
    path('form_trade/', views.formTrade, name="form-trade"),
    path('card/', views.cardInfo, name="card"),
    path('wonder/', views.wonder, name="wonder"),
    path('download/', views.download, name="blog-download"),
    path('sitemap.xml', views.sitemap, name="blog-sitemap"),
]
