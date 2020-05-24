import django_filters
from .models import Reservation
from .models import Room
from .models import User

class reservationFilter(django_filters.FilterSet):



    class Meta:
        model = Reservation
        fields = {
            'room':['icontains'],
            }

