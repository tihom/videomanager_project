from django.contrib.auth.models import User
from .models import Volunteer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',)

class VolunteerSerializer(serializers.ModelSerializer):
    # field from the user model
    username = serializers.CharField(source='user.username', required=False)
    email = serializers.CharField(source='user.email', required=False)
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)

    class Meta:
        model = Volunteer
        fields = ('user_id', 'username', 'email', 'first_name', 'last_name',
            'phone_number', 'leader') 
