from django.db import models

# Create your models here.
from diago.users.models import User


class Team(models.Model):
    id = models.CharField(max_length=120, unique=True, primary_key=True)
    name = models.CharField(max_length=120)
    team_leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # team_members =