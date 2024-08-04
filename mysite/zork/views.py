from django.shortcuts import render, redirect
from .models import Monster, Player, Room, Quesion, Battle, User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def error(request):
    return render(request, 'error.html')

def startgame(request):
    form = RegisterForm()
    current_room_num = Room.objects.first()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            form.save()
            user = authenticate(request, username=username, password=password1)
            if user:
                player = Player.objects.create(attack=20, defense=10, health=75, user=user, currentroom=current_room_num)
                player.save()
                login(request, user)
            return redirect("battle")
    return render(request, 'startgame.html', {"form":form})

def battle(request):
    current_player = Player.objects.get(user=request.user)
    battle = Battle.objects.all()
    current_room_num = Room.objects.first() 
    current_monster = Monster.objects.first()
    if "answered_quesion" not in request.session:
        request.session["answered_quesion"] = []
    answered_quesion = request.session["answered_quesion"]
    current_quesion = Quesion.objects.exclude(id__in = answered_quesion)
    if not current_quesion.exists():
         return redirect("error")
    quesion = random.choice(current_quesion)
    print(current_quesion, quesion, answered_quesion)
    if request.method == "POST":
        player_answer = request.POST["player_answer"]
        print(player_answer, quesion.answer)
        if player_answer.lower() == quesion.answer.lower():
            answered_quesion.append(quesion.id)
            request.session["answered_quesion"] = answered_quesion
            current_monster.health = current_monster.health + current_monster.defense - current_player.attack
            current_monster.save()
            messages.warning(request, "You are right")
            return redirect("battle")
        else: 
            answered_quesion.append(quesion.id)
            current_player.health = current_player.health + current_player.defense - current_monster.attack
            current_player.save()
            messages.error(request, "You are wrong")
            return redirect("battle")
    return render(request, 'battle.html', {'current_quesion':quesion, 'current_monster': current_monster, 'current_room_num': current_room_num, 'quesion':quesion, 'battle':battle, 'player': current_player})

