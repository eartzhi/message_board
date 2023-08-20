from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, \
  DateFilter, CharFilter, ChoiceFilter
from .models import Response
from django.forms import DateInput, DateTimeInput


class ResponseFilter(FilterSet):
    response_author = ModelChoiceFilter(
        field_name='response_author',
        queryset=Response.objects.all(),
        label='Автор статьи',
        empty_label='любой',
    )

    from_response_creation_time = DateTimeFilter(
        field_name='response_creation_time',
        label='С даты',
        lookup_expr='gte',
        widget=DateTimeInput(attrs={'type': 'date'})
    )

    to_response_creation_time = DateFilter(
        field_name='response_creation_time',
        label='До даты',
        lookup_expr='lte',
        widget=DateTimeInput(attrs={'type': 'date'})
    )

    response_text = CharFilter(
        field_name='response_text',
        label='Текст статьи содержит',
        lookup_expr='icontains',
    )

    class Meta:
        model = Response
        fields = [
            'response_text',
            'response_author',
            'from_response_creation_time',
            'to_response_creation_time'
        ]