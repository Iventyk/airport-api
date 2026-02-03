from django.contrib import admin
from flights.models import (
    Route,
    AirplaneType,
    Airplane,
    Crew,
    Flight,
)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("id", "source", "destination", "distance")
    search_fields = ("source__name", "destination__name")
    list_filter = ("source", "destination")


@admin.register(AirplaneType)
class AirplaneTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "airplane_type", "rows", "seats_in_row")
    list_filter = ("airplane_type",)
    search_fields = ("name",)


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "route",
        "airplane",
        "departure_time",
        "arrival_time",
    )
    list_filter = ("route", "airplane")
    filter_horizontal = ("crew",)
