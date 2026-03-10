from rest_framework import serializers
from .models import Bus, Seat, Booking

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id','seat_number','is_booked']

class BusSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)
    class Meta:
        model = Bus
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user','bus','seat','booking_time']
