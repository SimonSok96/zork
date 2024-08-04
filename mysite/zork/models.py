from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    number = models.IntegerField()
    quesion = models.ManyToManyField('Quesion')
    atherrooms = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class Monster(models.Model):
    attack = models.IntegerField()
    defense = models.IntegerField()
    health = models.IntegerField(default=100)
    drop = models.CharField(max_length=250)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Player(models.Model):
    attack = models.IntegerField()
    defense = models.IntegerField()
    health = models.IntegerField(default=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentroom = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    
class Battle(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    
class Quesion(models.Model):
    quesion = models.CharField(max_length=250)
    answer = models.CharField(max_length=250, null=True, blank=True)

    