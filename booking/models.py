from django.db import models
from user.models import SiteUser

class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_name

class Seat(models.Model):
    bus = models.ForeignKey(Bus, related_name='seats', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bus.bus_name} - {self.seat_number}"

class Booking(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.bus.bus_name} - {self.seat.seat_number}"
