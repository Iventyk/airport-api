from rest_framework.viewsets import ModelViewSet

from airports.models import Airport
from airports.serializers import AirportSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
