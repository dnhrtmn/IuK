from rest_framework import serializers

from . import models


class reservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Reservation
        fields = [
            "last_updated",
            "end_time",
            "created",
            "start_time",
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
