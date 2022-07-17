from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Role(models.TextChoices):
        USER = "USR", _("User")
        TEAM_MEMBER = "MBR", _("Team Member")
        TEAM_LEADER = "LDR", _("Team Leader")

    role = models.CharField(max_length=120,
                            choices=Role.choices,
                            default=Role.USER)
