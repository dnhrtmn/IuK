from rest_framework import serializers

from . import models


class reservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reservation
        fields = [
            "start_time",
            "room",
            "block",
            "created_by",
            "identifier",
        ]

class roomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = [
            "created",
            "last_updated",
            "description",
            "location",
            "size",
        ]
