from django.urls import path
from . import views

urlpatterns = [
    path('startgame/', views.startgame, name='startgame'),
    path('', views.home, name='home'),
]