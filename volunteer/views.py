from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers

from .models import Volunteer
from .serializers import VolunteerSerializer, UserSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    lookup_field = 'user_id'

    def get_permissions(self):
        # Authentication logic here
        if self.action in ('lookupuser',):
            self.permission_classes = [IsAuthenticated, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(self.__class__, self).get_permissions()

    def lookupuser(self, request):
        """
        Get currently logged in user
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def get_team(self, request):
        """
        Get the team of currently logged user
        """
        serializer = VolunteerSerializer(request.user.team, many=True)
        return Response(serializer.data)

    def add_team_member(self, request):
        """
        Post to add new team member
        """
        leader = request.user
        # check if username is not taken already
        new_username = request.data["username"]
        if User.objects.filter(username=new_username).exists():
            raise serializers.ValidationError('User already exists')
        # valdiate form data
        volunteer_serializer = VolunteerSerializer(volunteer, data=request.data, partial=True)
        volunteer_serializer.is_valid(raise_exception=True)
        validated_data = volunteer_serializer.validated_data
        # create user
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        # create volunteer
        validated_data["user"] = user
        validated_data["leader"] = leader
        volunteer_serializer.save()

        return Response(volunteer_serializer.data)

    def update_team_member(self, request, user_id):
        ''''
        Update team member
        '''
        leader = request.user
        # check if user exists
        user = User.objects.get(pk=user_id)
        if not user:
            raise serializers.ValidationError('User does not exist')
        # chck if authenticted user is the leader of user
        volunteer = user.volunteer
        if not volunteer and volunteer.leader != leader:
            raise serializers.ValidationError('User not part of your team')
        # validate form data
        volunteer_serializer = VolunteerSerializer(volunteer, data=request.data, partial=True)
        volunteer_serializer.is_valid(raise_exception=True)
        validated_data = volunteer_serializer.validated_data
        # update user
        user_data = validated_data.pop("user")
        user_serializer = UserSerializer(user, data=user_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        # update volunteer
        validated_data["user"] = user
        validated_data["leader"] = leader
        volunteer_serializer.save()

        return Response(volunteer_serializer.data)

    def delete_team_member(self, request, user_id):
        leader = request.user
        # check if user exists
        user = User.objects.get(pk=user_id)
        if not user:
            raise serializers.ValidationError('User does not exist')
        # chck if authenticted user is the leader of user
        volunteer = user.volunteer
        if not volunteer and volunteer.leader != leader:
            raise serializers.ValidationError('User not part of your team')
            
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



