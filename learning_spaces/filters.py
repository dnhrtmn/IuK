import django_filters
from .models import reservation
from .models import room
from .models import User

class reservationFilter(django_filters.FilterSet):



    class Meta:
        model = reservation
        fields = {
            'room':['icontains'],
            }

