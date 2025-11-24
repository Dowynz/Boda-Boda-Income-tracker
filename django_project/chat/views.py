from django.shortcuts import render, redirect
import json, os
BASE = os.path.dirname(os.path.dirname(__file__))
ROOMS_FILE = os.path.join(BASE, 'rooms.json')
def index(request):
    query = request.GET.get('q','')
    rooms = []
    if os.path.exists(ROOMS_FILE):
        with open(ROOMS_FILE,'r') as f:
            rooms = json.load(f)
    if query:
        rooms = [r for r in rooms if query.lower() in r['name'].lower()]
    if request.method == 'POST':
        username = request.POST.get('username')
        room_name = request.POST.get('room_name')
        # save room if new
        if not any(r['name']==room_name for r in rooms):
            rooms.append({'name':room_name})
            with open(ROOMS_FILE,'w') as f:
                json.dump(rooms,f)
        return redirect('room', room_name=room_name, username=username)
    return render(request,'chat/index.html',{'rooms':rooms,'query':query})
def room(request, room_name, username):
    return render(request,'chat/room.html',{'room_name':room_name,'username':username})
