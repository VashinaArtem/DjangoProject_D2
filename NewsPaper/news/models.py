from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.SmallIntegerField(default=0)

    def updaterating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rate'))
        pRat = 0
        pRat = postRat.get('rate')

        commentRat = self.user.comment_set.aggregate(commentRating=Sum('rate'))
        cRat = 0
        cRat += commentRat.get('rate')

        self.rate = pRat * 3 + cRat
        self.save()



class Category(models.Model):
    theme = models.CharField(max_length=64, default='NO THEME', unique=True)

    def __str__(self):
        return self.theme

class Post(models.Model):
    NEWS = 'NW'
    Article = 'AR'
    CHOICES = [
        ("ARTICLE", 'Статья'),
        ("NEWS", 'Новость')
    ]
    info_type = models.CharField(max_length=7, choices=CHOICES, error_messages='NO TYPE OF INFO')

    creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=32, default='NO TITLE')
    text = models.TextField()
    rate = models.SmallIntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]}...{self.rate}'

    def __str__(self):
        return f'date: {self.creation_date}, author: {self.author}, text:{self.text[0:123]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField(max_length=5000)
    creation_date = models.DateField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()












