from django.contrib import admin
from .models import Room, Monster, Player, Battle, Quesion

# Register your models here.

admin.site.register(Room)
admin.site.register(Monster)
admin.site.register(Player)
admin.site.register(Battle)
admin.site.register(Quesion)