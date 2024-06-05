from django.db import models

# Create your models here.

class Room(models.Model):
    number = models.IntegerField()
    quesion = models.CharField()
    monster = models.CharField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    drop = models.CharField()
    
class Player(models.model):
    name = models.CharField()
    armor = models.