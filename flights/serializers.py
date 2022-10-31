from dataclasses import field, fields
from flights.models import Booking, Flight
from rest_framework import serializers


class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "destination", "time", "price"]

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["fligt", "date", "id"]