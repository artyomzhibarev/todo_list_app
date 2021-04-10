from django_filters import rest_framework as drf_filter

from .models import Note


class NoteFilter(drf_filter.FilterSet):
    by_important = drf_filter.BooleanFilter(field_name='important', )

    min_view = drf_filter.NumberFilter('views',
                                       lookup_expr='gte')
    max_view = drf_filter.NumberFilter('views',
                                       lookup_expr='lte')

    author = drf_filter.NumberFilter('author__pk', )

    author_name = drf_filter.CharFilter('author__username',
                                        lookup_expr='contains')

    by_public = drf_filter.BooleanFilter(field_name='public')

    class Meta:
        model = Note
        fields = ('by_important', 'by_public', 'min_view', 'max_view', 'author', 'author_name',)
