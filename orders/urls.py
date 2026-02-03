from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet, TicketViewSet


router = DefaultRouter()
router.register("orders", OrderViewSet, basename="orders")
router.register("tickets", TicketViewSet, basename="tickets")

urlpatterns = router.urls
