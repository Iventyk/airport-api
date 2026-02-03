from rest_framework.routers import DefaultRouter
from airports.views import AirportViewSet


router = DefaultRouter()
router.register("airports", AirportViewSet)

urlpatterns = router.urls
