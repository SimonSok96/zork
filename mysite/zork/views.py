from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def startgame(request):
    return render(request, 'startgame.html')