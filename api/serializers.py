from .models import Parking, Utilisateur
from rest_framework import serializers
from django.contrib.auth import authenticate

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id','email','nom','prenom','username')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id','email','username','password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Utilisateur.objects.create_user(**validated_data)
        return user