"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from flights.views import BookingDetailView, FlightListView, upcomingBookingListView,  BookingUpdateView, BookingDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", FlightListView.as_view(), name="flights-list"),
    path("bookings/", upcomingBookingListView.as_view(), name="bookings-list"),
    path("booking/<int:Booking_id>/", BookingDetailView.as_view(), name="booking-details"),
    path("booking/<int:Booking_id>/update/", BookingUpdateView.as_view(), name="update-booking"),
    path("booking/<int:Booking_id>/delete/", BookingDeleteView.as_view(), name="cancel-booking"),

]
