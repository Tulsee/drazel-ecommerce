from rest_framework import status, viewsets
from .seializers import BeerSerializer

from .models import Beer


class BeerProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
