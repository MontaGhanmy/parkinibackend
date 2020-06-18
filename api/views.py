from .models import Parking, Utilisateur , Voiture, Occupation, Place
from .serializers import ParkingSerializer, UtilisateurSerializer, RegisterSerializer,LoginSerializer , VoitureSerializer, OccupationSerializer, PlaceSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

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

# Get User API
class UserAPI(APIView):
  
  permission_classes = [permissions.IsAuthenticated,]
  serializer_class = UtilisateurSerializer

  def get(self, request):
    user = Utilisateur.objects.get(pk=request.user.pk)
    # the many param informs the serializer that it will be serializing more than a single article.
    serializer = UtilisateurSerializer(user, many=False)
    return Response(serializer.data)
  def put(self, request):
    user = Utilisateur.objects.get(pk=request.user.pk)
    data = request.data
    serializer = UtilisateurSerializer(instance=user, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
      user = serializer.save()
    return Response(serializer.data)

class Logout(generics.GenericAPIView):
  def post(self, request, format=None):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ParkingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def pre_save(self, obj):
        obj.parking_image = self.request.FILES.get('parking_image')

class VoitureViewSet(viewsets.ModelViewSet):
    queryset = Voiture.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoitureSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        return Voiture.objects.filter(owner=self.request.user)


class OccupationViewSet(viewsets.ModelViewSet):
  queryset = Occupation.objects.all()
  serializer_class = OccupationSerializer
  permission_classes = [permissions.IsAuthenticated]
  def get_queryset(self):
    return Occupation.objects.filter(voiture__owner=self.request.user)

class PlaceViewSet(viewsets.ModelViewSet):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer