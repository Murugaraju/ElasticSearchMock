from django.shortcuts import render

# Create your views here.

#belowfor dsl_drf
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .serializers import CarDocumnetSerializer
from mock.documents import CarDocument

class CarDocumentView(DocumentViewSet):
    document=CarDocument
    serializer_class=CarDocumnetSerializer
    lookup_field ='id'

    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'name',
        'color',
        'type',
        'id',
        'description',
        # 'country',
    )
    # Define filtering fields
    filter_fields = {
        'id': None,
        'name': 'name.raw',
        # 'city': 'city.raw',
        # 'state_province': 'state_province.raw',
        # 'country': 'country.raw',
    }
    # Define ordering fields
    ordering_fields = {
        'id': None,
        'name': None,
        # 'city': None,
        # 'country': None,
    }
    # Specify default ordering
    ordering = ('id', 'name',)

def search(request):
    q=request.GET.get('q')
