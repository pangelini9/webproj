from django.urls import path
from . import views

app_name = 'football'
urlpatterns = [
	path('', views.home, name='home'),
	path('teams/', views.teams, name='teams'),
	path('teams/<int:team_id>/', views.teamplayers, name='teamplayers'),
#	path('players/', views.players, name='players'),
]
