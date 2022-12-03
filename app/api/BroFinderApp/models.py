
from django.db import models

# Create your models here.

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=20)
    UserAddress = models.CharField(max_length=50, blank=True)
    UserDescription = models.CharField(max_length=300, blank=True)
    UserEvents = models.CharField(max_length=1000, blank=True)
    UserFavorites = models.CharField(max_length=1000, blank=True)
    UserFriends = models.CharField(max_length=1000, blank=True)
    UserOwnedEvents = models.CharField(max_length=1000, blank=True)

class Events(models.Model):
    EventId = models.AutoField(primary_key=True)
    EventName = models.CharField(max_length=50)
    EventAddress = models.CharField(max_length=50)
    EventDescription = models.CharField(max_length=300)
    EventOwner = models.CharField(max_length=100)
    EventDateOfCreate = models.DateField()
    EventDateOfEvent = models.DateField()
    EventMaxUsers = models.IntegerField()
    EventSignedUsers = models.CharField(max_length=1000, blank=True)
    EventFilter = models.CharField(max_length=50, blank=True)

class Comments(models.Model):
    CommentId = models.AutoField(primary_key=True)
    EventId = models.IntegerField()
    CommentText = models.CharField(max_length=500)
    CommentOwner = models.CharField(max_length=300)
    CommentDate = models.DateField()
    CommentLikes = models.CharField(max_length=500, blank=True)
