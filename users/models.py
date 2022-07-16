from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_team_leader = models.BooleanField(default=False)
    is_team_member = models.BooleanField(default=False)

    def clean(self):
        if self.is_team_leader and not self.is_team_member:
            self.is_team_member = True
    #todo validate that this gets executed from save