from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.exceptions import ValidationError  # ✅ Исправленный импорт

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        customer = serializer.validated_data['customer']
        date = serializer.validated_data['date']

        existing_reservation = Reservation.objects.filter(customer=customer, date=date).exists()
        if existing_reservation:
            raise ValidationError("This customer already has a reservation on this date.")  # ✅ Исправленная строка

        serializer.save()

class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

@api_view(['GET'])
def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(customer_id=user_id)
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_reservation_status(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    status = request.data.get('status')
    
    if status not in ["pending", "confirmed", "canceled"]:
        return Response({'error': 'Invalid status'}, status=400)
    
    reservation.status = status
    reservation.save()
    
    return Response({'message': 'Reservation status updated successfully'})

@api_view(['DELETE'])
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return Response({'message': 'Reservation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
