from django.db import models

# Create your models here.

class Team(models.Model):
    """ A class to describe a football team, with a name and a city """
    
    name = models.CharField(max_length=30);
    city = models.CharField(max_length=30);
    
    def __str__(self):
        """ method to determine what to write when the object is printed """
        return self.name;

class Player(models.Model):
    """ A class to describe football players """
    
    firstname = models.CharField(max_length = 20);
    lastname = models.CharField(max_length = 20);
    team = models.ForeignKey(Team, on_delete = models.CASCADE);
    
    def __str__(self):
        return self.firstname + " " + self.lastname;