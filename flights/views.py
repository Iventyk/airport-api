from rest_framework.viewsets import ModelViewSet
from flights.models import Route
from flights.serializers import RouteSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.select_related("source", "destination")
    serializer_class = RouteSerializer


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


class AirplaneTypeViewSet(ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class AirplaneViewSet(ModelViewSet):
    queryset = Airplane.objects.select_related("airplane_type")
    serializer_class = AirplaneSerializer


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class FlightViewSet(ModelViewSet):
    queryset = (
        Flight.objects
        .select_related("route", "airplane")
        .prefetch_related("crew")
    )
    serializer_class = FlightSerializer
