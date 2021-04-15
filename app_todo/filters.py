from django_filters import rest_framework as drf_filter

from .models import Note


class NoteFilter(drf_filter.FilterSet):
    by_important = drf_filter.BooleanFilter(field_name='important', )

    by_status = drf_filter.CharFilter(field_name='status', )

    min_view = drf_filter.NumberFilter('views',
                                       lookup_expr='gte')
    max_view = drf_filter.NumberFilter('views',
                                       lookup_expr='lte')

    author = drf_filter.NumberFilter('author__pk', )

    author_name = drf_filter.CharFilter('author__username',
                                        lookup_expr='contains')

    by_public = drf_filter.BooleanFilter(field_name='public')

    by_title_contain = drf_filter.CharFilter('title',
                                             lookup_expr='contains')

    class Meta:
        model = Note
        fields = ('by_important', 'by_status', 'by_public', 'min_view', 'max_view', 'author', 'author_name',
                  'by_title_contain')


class CommentFilter(drf_filter.FilterSet):
    by_rating = drf_filter.NumberFilter(field_name='rating')