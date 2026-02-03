from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from flights.models import (
    Route,
    AirplaneType,
    Airplane,
    Crew,
    Flight,
)
from flights.serializers import (
    RouteSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer,
    CrewSerializer,
    FlightSerializer,
)


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.select_related("source", "destination")
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AirplaneTypeViewSet(ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AirplaneViewSet(ModelViewSet):
    queryset = Airplane.objects.select_related("airplane_type")
    serializer_class = AirplaneSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FlightViewSet(ModelViewSet):
    queryset = (
        Flight.objects
        .select_related("route", "airplane")
        .prefetch_related("crew")
    )
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
