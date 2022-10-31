from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.serializers import FlightListSerializer, BookingListSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class upcomingBookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer

