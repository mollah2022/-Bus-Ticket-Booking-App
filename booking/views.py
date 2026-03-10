from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Bus, Seat, Booking
from .serializers import BusSerializer, BookingSerializer

# ----------------- Bus Views -----------------
class BusListCreateView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class BusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

# ----------------- Booking Views -----------------
class BookingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        seat_id = request.data.get('seat')
        try:
            seat = Seat.objects.get(id=seat_id)
            if seat.is_booked:
                return Response({'error':'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)

            seat.is_booked = True
            seat.save()

            booking = Booking.objects.create(
                user=request.user,
                bus=seat.bus,
                seat=seat
            )
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Seat.DoesNotExist:
            return Response({'error':'Invalid Seat ID'}, status=status.HTTP_400_BAD_REQUEST)

class UserBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
