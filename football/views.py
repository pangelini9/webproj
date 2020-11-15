from django.shortcuts import render

from .models import Team, Player

# Create your views here.

def home(request):
    """ the homepage of the football app """
    return render(request, 'football/index.html');

def teams(request):
    teamsList = Team.objects.order_by('id')
    context = {'teams' : teamsList}
    return render(request, 'football/teams.html', context)

def players(request):
    teamName = "Man United"
    team = Team.objects.get(name=teamName);
    playersList = team.player_set.all();
    context = {'players' : playersList, 'team' : team}
    return render(request, 'football/players.html', context)

def teamplayers(request, team_id):
    team = Team.objects.get(id=team_id);
    playersList = team.player_set.all();
    context = {'players' : playersList, 'team' : team}
    return render(request, 'football/players.html', context)