from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    return render(request,'home.html')
#to access room 
def room(request,room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)

    return render(request,'room.html',{'username':username,'room':room,'room_details':room_details})

def checkroom(request):
    room=request.POST['room_name']
    username=request.POST['username']
#checking if room exists
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
#creating new room
        new_room=Room.objects.create(name=room)
        new_room.save()
        #generate url for a particular rool with username data
        return redirect('/'+room+'/?username='+username)
#adds messages entered into the messages module
def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    print(message,username,room_id)
    new_message=Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()

    return HttpResponse('Message sent successfully')
#to get messages from the database related to a particular room
def getMessages(request,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)

    return JsonResponse({'messages':list(messages.values())})

