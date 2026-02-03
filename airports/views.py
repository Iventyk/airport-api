from rest_framework.viewsets import ModelViewSet
from airports.models import Airport
from airports.serializers import AirportSerializer


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
