from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from flights.serializers import FlightListSerializer, BookingListSerializer, BookingCreateSerializer, BookingDetailSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer

class upcomingBookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "Booking_id"

class CreateBookingView(CreateAPIView):
    serializer_class = BookingCreateSerializer

class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "Booking_id"

class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "Booking_id"



