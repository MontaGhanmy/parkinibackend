from .models import Parking
from .serializers import ParkingSerializer
from rest_framework import viewsets

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializerl
