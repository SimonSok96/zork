from django.shortcuts import render
from .models import Monster, Player, Room, Quesion, Battle

# Create your views here.

def home(request):
    return render(request, 'home.html')


def startgame(request):
    return render(request, 'startgame.html')

def battle(request):
    current_player = Player.objects.first()
    quesion = Quesion.objects.all()
    battle = Battle.objects.all()
    current_room_num = Room.objects.first() 
    current_quesion = current_room_num.quesion.order_by('?')[0]
    print(current_quesion)
    current_monster = Monster.objects.first()
    return render(request, 'battle.html', {'current_quesion':current_quesion, 'current_monster': current_monster, 'current_room_num': current_room_num, 'quesion':quesion, 'battle':battle})