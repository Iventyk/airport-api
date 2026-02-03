from rest_framework.viewsets import ModelViewSet
from flights.models import Route
from flights.serializers import RouteSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.select_related("source", "destination")
    serializer_class = RouteSerializer
