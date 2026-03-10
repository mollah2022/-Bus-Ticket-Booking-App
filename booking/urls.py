from django.urls import path
from .views import BusListCreateView, BusDetailView, BookingView, UserBookingView



urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='bus-list'),
    path('buses/<int:pk>/', BusDetailView.as_view(), name='bus-detail'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('my-bookings/', UserBookingView.as_view(), name='user-bookings'),
]
