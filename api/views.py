from .models import Parking, Utilisateur
from knox.models import AuthToken
from .serializers import ParkingSerializer, UtilisateurSerializer, RegisterSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response

class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UtilisateurSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ParkingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)