from .models import Parking, Utilisateur
from .serializers import ParkingSerializer, UtilisateurSerializer, RegisterSerializer, LoginSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# USER REGISTER
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      "user": UtilisateurSerializer(user, context=self.get_serializer_context()).data,
      "token": token.key
    })

# USER LOGIN
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      "user": UtilisateurSerializer(user, context=self.get_serializer_context()).data,
      "token": token.key
    })

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ParkingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)