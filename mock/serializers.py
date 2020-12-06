# Dynamic searlizer for Cars documents
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import CarDocument
class CarDocumnetSerializer(DocumentSerializer):
    class Meta:
        document=CarDocument
        fields=(
               'id',
              'name',
        'color',
        'type',
     
        'description',
        )
