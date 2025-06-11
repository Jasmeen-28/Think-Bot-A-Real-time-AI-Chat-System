from django.shortcuts import render
from .models import Chat, Group
# Create your views here.

def index(request, room_name):
    return render(request, 'app/index.html', {
        'room_name':room_name
    })

def login(request):
    return render(request, 'app/index.html')

def signup(request):
    return render(request, 'app/signup.html')