from rest_framework import serializers
from BroFinderApp.models import Users,Events,Comments
from django.contrib.auth.models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users 
        fields=('UserId','UserName','UserAddress','UserDescription','UserEvents','UserFavorites','UserFriends','UserOwnedEvents')

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events 
        fields=('EventId','EventName','EventAddress','EventDescription','EventOwner','EventDateOfCreate','EventDateOfEvent','EventMaxUsers','EventSignedUsers','EventFilter')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=('id','password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments 
        fields=('CommentId','EventId','CommentText','CommentOwner','CommentDate','CommentLikes')
