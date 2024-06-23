from django.urls import path
from . import views

urlpatterns = [
    path('startgame/', views.startgame, name='startgame'),
    path('battle/', views.battle, name='battle'),
    path('', views.home, name='home'),
]