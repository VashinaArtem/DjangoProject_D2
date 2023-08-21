# Добавьте страницу /news/search.
# На ней должна быть реализована возможность
# искать новости по определённым критериям.
# Критерии должны быть следующие:
# по названию;
# по категории;
# позже указываемой даты.

from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):

    added_after = DateTimeFilter(
        field_name='creation_date',
        lookup_expr='gt',
        widget=DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'})
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            #'category': ['icontains'],
            'postcategory__category' : ['exact']
        }

