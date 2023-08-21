from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy

class PostsList(ListView):
    model = Post
    ordering = 'creation_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



class NewsPostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_post_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'Новость'
        return super().form_valid(form)


class ArticlePostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_post_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'Статья'
        return super().form_valid(form)


class NewsPostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_post_update.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'Новость'
        return super().form_valid(form)


class ArticlePostUpdate(UpdateView):
    from_class = PostForm
    model = Post
    template_name = 'article_post_update.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'Статья'
        return super().form_valid(form)

class NewsPostDelete(DeleteView):
    model = Post
    template_name = 'news_post_delete.html'
    success_url = reverse_lazy('post_list')
class ArticlePostDelete(DeleteView):
    model = Post
    template_name = 'article_post_delete.html'
    success_url = reverse_lazy('post_list')











