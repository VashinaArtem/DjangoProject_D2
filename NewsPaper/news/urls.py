from django.urls import path
from .views import PostsList, PostDetail, NewsPostCreate, ArticlePostCreate, ArticlePostUpdate, NewsPostUpdate, NewsPostDelete, ArticlePostDelete
from .models import *

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),

   path('news/create/', NewsPostCreate.as_view(), name='news_post_create'),
   path('articles/create/', ArticlePostCreate.as_view(), name='article_post_create'),

   path('news/<int:pk>/edit/', NewsPostUpdate.as_view(model=Post, fields=['title', 'text', 'rate', 'author']), name='news_post_update'),
   path('articles/<int:pk>/edit/', ArticlePostUpdate.as_view(model=Post, fields=['title', 'text', 'rate', 'author']), name='article_post_update'),

   path('news/<int:pk>/delete/', NewsPostDelete.as_view(), name='news_post_delete'),
   path('articles/<int:pk>/delete/', ArticlePostDelete.as_view(), name='article_post_delete'),

]



