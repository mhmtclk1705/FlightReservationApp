from django.shortcuts import render
from flight.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer, StaffFlightSerializer
from flight.models import Flight, Passenger, Reservation
from rest_framework import viewsets
from .permission import IsStafforReadOnly
from datetime import datetime,date
# Create your views here.

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer
    
    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()

        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset= Flight.object.filter(date_of_departure__gt=today)
            if Flight.objects.filter(date_of_departure=today):
                today_qs = Flight.objects.filter(date_of_departure=today).filter(etd__gt=current_time)
                queryset = queryset.union(today_qs)
            return queryset






class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.objects.filter(user=self.request.user)