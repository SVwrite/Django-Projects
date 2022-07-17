from django.db import models

# Create your models here.


class Team(models.Model):
    """
        class Role(models.TextChoices):
        USER = "USR", _("User")
        TEAM_MEMBER = "MBR", _("Team Member")
        TEAM_LEADER = "LDR", _("Team Leader")

    role = models.CharField(max_length=120,
                            choices=Role.choices,
                            default=Role.USER)
    """
    id = models.CharField(max_length=120, unique=True, primary_key=True)
    name = models.CharField(max_length=120)
    team_leader = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name="team_leader")
    team_members = models.ManyToManyField('users.User', related_name="team_members")

    def clean(self):
        pass
        # print(self.team_leader.role, self.team_leader.Role.)
        self.team_leader.role = self.team_leader.Role.TEAM_LEADER
        for member in self.team_members.all():
            if member == self.team_leader:
                break
        self.team_members.remove(member)

    def __str__(self):
        print(type(self.team_members.all()))
        members = [mem.username for mem in self.team_members.all()]
        return f"{self.name} {members}"
