from rest_framework import status, viewsets
from .seializers import BeerSerializer
from django_filters.rest_framework import DjangoFilterBackend

from .models import Beer


class BeerProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'country_of_origin', 'abv', 'brand']
