from rest_framework import viewsets, permissions

from . import serializers
from . import models


class reservationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Reservation class"""

    queryset = models.Reservation.objects.all()
    serializer_class = serializers.reservationSerializer
    permission_classes = [permissions.IsAuthenticated]


class roomViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Room.objects.all()
    serializer_class = serializers.roomSerializer
    permission_classes = [permissions.IsAuthenticated]
