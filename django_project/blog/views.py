from .models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': '營隊簡介'})


def intro(request):
    return render(request, 'blog/intro.html', {'title': '營隊課程'})


def apply(request):
    return render(request, 'blog/apply.html', {'title': '報名'})


def faq(request):
    return render(request, 'blog/faq.html', {'title': '常見問題'})


def download(request):
    return render(request, 'blog/download.html', {'title': '下載專區'})


def game(request):
    return render(request, 'blog/game.html', {'title': '營期首頁'})


def formEcon(request):
    return render(request, 'blog/econ.html', {'title': '伊康攻略表單'})


def formTrade(request):
    return render(request, 'blog/trade.html', {'title': '系統貿易表單'})


def cardInfo(request):
    return render(request, 'blog/card.html', {'title': '卡片資訊'})


def wonder(request):
    return render(request, 'blog/wonder.html', {'title': '世界奇觀'})


def sitemap(request):
    return render(request, 'blog/sitemap.xml')
