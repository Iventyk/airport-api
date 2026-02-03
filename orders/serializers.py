from rest_framework import serializers
from orders.models import Order, Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "flight",
            "row",
            "seat",
        )


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, source="ticket_set", read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "tickets",
        )
