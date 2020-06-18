from .models import Parking, Utilisateur , Voiture, Occupation, Place
from rest_framework import serializers
from django.contrib.auth import authenticate

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id','email','nom','prenom','username','password','num_tel')
        extra_kwargs = {'password': {'write_only': True}}

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id','email','username','password','num_tel','nom','prenom')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Utilisateur.objects.create_user(validated_data['email'],validated_data['username'],validated_data['password'])
        user.nom = validated_data['nom']
        user.prenom = validated_data['prenom']
        user.num_tel = validated_data['num_tel']
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Verify your credentials!")

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = '__all__'

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'