from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'phone_number', 'company', 'role']
        
    def validate_age(self, value):
        if value < 0:
            return serializers.ValidationError('Age Cannot be Negative.')
        return value

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'profile']
        extra_kwargs = {'password' : {'write_only' : True}}
        
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        user = User(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        Profile.objects.create(user = user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        
        instance.first_name = validated_data.get('first_name', validated_data.first_name)
        instance.last_name = validated_data.get('last_name', validated_data.last_name)
        instance.email = validated_data.get('email', validated_data.email)
        instance.username = validated_data.get('username', validated_data.username)
        instance.save()
        
        if profile_data:
            profile = instance.profile
            profile.age = profile_data.get('age', profile.bio)
            profile.role = profile_data.get('role', profile.role)
            profile.company = profile_data.get('company', profile.company)
            profile.phone_number = profile_data.get('phone_number', profile.phone_number)

class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)