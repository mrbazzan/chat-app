
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Room, Message
# Create your views here.


def home(request):
    return render(request, "home.html")


def room(request, room):
    user_name = request.GET.get('username')
    room = Room.objects.get(slug=room)
    
    return render(request, "root.html", {
        'username': user_name,
        'room_details': room,
    })


def check_view(request):
    username = request.POST.get("username")
    room_name = request.POST.get("room_name")
    try:
        room = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        room = Room(name=room_name)
        room.save()
    
    return redirect(f"/{room.slug}/?username={username}")


def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')

    message = Message(
        user_message=message,
        user=username,
        room=Room.objects.get(id=room_id)
    )
    message.save()
    return HttpResponse("Message sent")


def getMessages(request, room_id):
    messages = Message.objects.filter(room=Room.objects.get(id=room_id))
    _messages = []
    for message in messages:
        _messages.append(
            {
            "date": message.date,
            "user_message": message.user_message,
            "user": message.user
        })
    return JsonResponse({"messages": _messages})