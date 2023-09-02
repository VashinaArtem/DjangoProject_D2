# Добавьте страницу /news/search.
# На ней должна быть реализована возможность
# искать новости по определённым критериям.
# Критерии должны быть следующие:
# по названию;
# по категории;
# позже указываемой даты.

from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category

class PostFilter(FilterSet):

    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
    )

    added_after = DateTimeFilter(
        field_name='creation_date',
        lookup_expr='gt',
        widget=DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'})
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'text' : ['icontains'],
        }

