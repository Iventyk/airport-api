from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from orders.models import Order, Ticket
from orders.serializers import OrderSerializer, TicketSerializer
from orders.permissions import IsOwner


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Ticket.objects.filter(order__user=self.request.user)
