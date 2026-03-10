from django.contrib import admin
from .models import Bus, Seat, Booking

# ---------------- Bus Admin ----------------
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus_name', 'number', 'origin', 'destination')
    search_fields = ('bus_name', 'number', 'origin', 'destination')

# ---------------- Seat Admin ----------------
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'seat_number', 'is_booked')
    list_filter = ('bus', 'is_booked')
    search_fields = ('seat_number',)

# ---------------- Booking Admin ----------------
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bus', 'seat', 'booking_time')
    list_filter = ('bus', 'booking_time')
    search_fields = ('user__username', 'bus__bus_name', 'seat__seat_number')
