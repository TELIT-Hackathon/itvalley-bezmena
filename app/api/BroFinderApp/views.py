from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BroFinderApp.models import Users,Events,Comments
from BroFinderApp.serializers import UsersSerializer,EventsSerializer,UserSerializer,CommentSerializer

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.core.files.storage import default_storage
import os

# Create your views here.

@csrf_exempt
def getUsers(request,name):
    if request.method=='GET':
        users = User.objects.filter(username=name)
        user_serializer=UserSerializer(users,many=True)
        return JsonResponse(user_serializer.data,safe=False)
    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        users=User.objects.get(id=users_data['id'])
        user_serializer=UserSerializer(users,data=users_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

@csrf_exempt
def loginuser(request,id=0):
    if request.method=='POST':
        json=JSONParser().parse(request)
        username = json['UserName']
        password = json['UserPassword']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return JsonResponse(username+" "+password,safe=False)
        else:
            return JsonResponse("Chyba",safe=False)


@csrf_exempt
def registeruser(request,id=0):
    if request.method=='POST':
        json=JSONParser().parse(request)
        username = json['UserName']
        password = json['UserPassword']
        email = json['UserEmail']
        user = User.objects.create_user(username=username,email=email,password=password)
        return JsonResponse("Ok",safe=False)



@csrf_exempt
def logoutuser(request,id=0):
    logout(request)
    return JsonResponse("Ok",safe=False)


@csrf_exempt
def usersApi(request,id=0):
    if request.method=='GET':
        users = Users.objects.all()
        users_serializer=UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method=='POST':
        users_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        users=Users.objects.get(UserId=users_data['UserId'])
        users_serializer=UsersSerializer(users,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        users=Users.objects.get(UserId=id)
        users.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def pokusApi(request,name):
    if request.method=='GET':
        users = Users.objects.filter(UserName=name)
        users_serializer=UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        users=Users.objects.get(UserId=users_data['UserId'])
        user_serializer=UsersSerializer(users,data=users_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")

@csrf_exempt
def eventikApi(request,name):
    if request.method=='GET':
        event=Events.objects.filter(EventFilter=name)
        events_serializer=EventsSerializer(event,many=True)
        return JsonResponse(events_serializer.data,safe=False)

@csrf_exempt
def eventsApi(request,id=0):
    if request.method=='GET':
        if id==0:
            events = Events.objects.all()
            events_serializer=EventsSerializer(events,many=True)
            return JsonResponse(events_serializer.data,safe=False)
        else:
            event=Events.objects.filter(EventId=id)
            events_serializer=EventsSerializer(event,many=True)
            return JsonResponse(events_serializer.data,safe=False)
    elif request.method=='POST':
        event_data=JSONParser().parse(request)
        events_serializer=EventsSerializer(data=event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse(events_serializer.data['EventId'],safe=False)
        return JsonResponse("Failed to Adds",safe=False)
    elif request.method=='PUT':
        event_data=JSONParser().parse(request)
        event=Events.objects.get(EventId=event_data['EventId'])
        events_serializer=EventsSerializer(event,data=event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        event=Events.objects.get(EventId=id)
        event.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def commentApi(request,id=0):
    if request.method=='GET':
        if id==0:
            comments = Comments.objects.all()
            comment_serializer=CommentSerializer(comments,many=True)
            return JsonResponse(comment_serializer.data,safe=False)
        else:
            comments = Comments.objects.filter(EventId=id)
            comment_serializer=CommentSerializer(comments,many=True)
            return JsonResponse(comment_serializer.data,safe=False)
    elif request.method=='POST':
        comment_data=JSONParser().parse(request)
        comment_serializer=CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data['CommentId'],safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        comment_data=JSONParser().parse(request)
        comment=Comments.objects.get(CommentId=comment_data['CommentId'])
        comment_serializer=CommentSerializer(comment,data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        comment=Comments.objects.get(CommentId=id)
        comment.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def kommentApi(request,id=0):
    if request.method=='GET':
        if id==0:
            comments = Comments.objects.all()
            comment_serializer=CommentSerializer(comments,many=True)
            return JsonResponse(comment_serializer.data,safe=False)
        else:
            comments = Comments.objects.filter(CommentId=id)
            comment_serializer=CommentSerializer(comments,many=True)
            return JsonResponse(comment_serializer.data,safe=False)
    elif request.method=='POST':
        comment_data=JSONParser().parse(request)
        comment_serializer=CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data['CommentId'],safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        comment_data=JSONParser().parse(request)
        comment=Comments.objects.get(CommentId=comment_data['CommentId'])
        comment_serializer=CommentSerializer(comment,data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        comment=Comments.objects.get(CommentId=id)
        comment.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    # print(os.path.join(os.path.join(os.getcwd(),"Photos"),request.get_full_path().split("/")[-1]+".jpg"))
    # print(os.path.exists(os.path.join(os.path.join(os.getcwd(),"Photos"),request.get_full_path().split("/")[-1]+".jpg")))
    if os.path.exists(os.path.join(os.path.join(os.getcwd(),"Photos"),request.get_full_path().split("/")[-1]+".jpg"))==False:
        pass
    else:
        os.remove(os.path.join(os.path.join(os.getcwd(),"Photos"),request.get_full_path().split("/")[-1]+".jpg"))
    os.rename(os.path.join(os.path.join(os.getcwd(),"Photos"),file.name),os.path.join(os.path.join(os.getcwd(),"Photos"),request.get_full_path().split("/")[-1]+".jpg"))
    return JsonResponse(file_name,safe=False)


@csrf_exempt
def orderedEventsApi(request,id=0):
    if request.method=='GET':
        if id=="1":
            events = Events.objects.order_by('EventDateOfEvent')
            events_serializer=EventsSerializer(events,many=True)
            return JsonResponse(events_serializer.data,safe=False)
        elif id=="2":
            events = Events.objects.order_by('-EventDateOfCreate')
            events_serializer=EventsSerializer(events,many=True)
            return JsonResponse(events_serializer.data,safe=False)
        elif id=="3":
            events = Events.objects.order_by('-EventMaxUsers')
            events_serializer=EventsSerializer(events,many=True)
            return JsonResponse(events_serializer.data,safe=False)


@csrf_exempt
def eventikNameApi(request,name):
    if request.method=='GET':
        event=Events.objects.filter(EventName=name)
        events_serializer=EventsSerializer(event,many=True)
        print(events_serializer.data[0]['EventId'])
        return JsonResponse(events_serializer.data[0]['EventId'],safe=False)