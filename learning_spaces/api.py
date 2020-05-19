from rest_framework import viewsets, permissions

from . import serializers
from . import models


class reservationViewSet(viewsets.ModelViewSet):
    """ViewSet for the reservation class"""

    queryset = models.reservation.objects.all()
    serializer_class = serializers.reservationSerializer
    permission_classes = [permissions.IsAuthenticated]


class roomViewSet(viewsets.ModelViewSet):
    """ViewSet for the room class"""

    queryset = models.room.objects.all()
    serializer_class = serializers.roomSerializer
    permission_classes = [permissions.IsAuthenticated]
