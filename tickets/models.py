from django.utils.translation import gettext_lazy as _
from django.db import models

from team.models import Team
from users.models import User


class Ticket(models.Model):

    class TicketStatus(models.TextChoices):
        ASSIGNED = "AS", _("Assigned")
        IN_PROGRESS = "IP", _("In Progress")
        UNDER_REVIEW = "UR", _("Under Review")
        DONE = "DN", _("Done")

    name = models.CharField(max_length=120)
    description = models.TextField()
    team = models.ForeignKey(to=Team,
                             on_delete=models.SET_NULL,
                             null=True)
    team_member = models.ForeignKey(to=User, blank=True, on_delete=models.SET_NULL, null=True)
    status = models.CharField(blank=True,
                              max_length=120,
                              choices=TicketStatus.choices,
                              default=TicketStatus.ASSIGNED)
    started_at = models.DateTimeField(blank=True)
    finished_at = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name
