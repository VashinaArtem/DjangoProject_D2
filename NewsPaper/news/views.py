from .models import Post
from .filters import PostFilter
from .forms import PostForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import(
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

class PostsList(ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'posts.html'
    context_object_name = 'posts' # пременная контекста для post.html
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset() #получаю данные из бд
        self.filterset = PostFilter(self.request.GET, queryset) # передача данных в фильтр
        return self.filterset.qs # получаем отфильтрованные данные

    def get_context_data(self, *, object_list=None, **kwargs): # для вывода новых переменных на странице
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        #context['registr'] = True
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



class NewsPostCreate(CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_post_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'NEWS'
        return super().form_valid(form)


class ArticlePostCreate(CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'article_post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'ARTICLE'
        return super().form_valid(form)


class NewsPostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_post_update.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'NEWS'
        return super().form_valid(form)


class ArticlePostUpdate(PermissionRequiredMixin, UpdateView):
    from_class = PostForm
    model = Post
    template_name = 'article_post_update.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'ARTICLE'
        return super().form_valid(form)


class NewsPostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'news_post_delete.html'
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'NEWS'
        return super().form_valid(form)



class ArticlePostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'article_post_delete.html'
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        post = form.save(commit=False)
        post.info_type = 'ARTICLE'
        return super().form_valid(form)


# def news_post_create(request):
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.info_type = 'Новость'
#         return super().form_valid(form)
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news/')
#     return render(request, 'news_post_edit.html', {'form':form})








