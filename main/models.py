from django.utils import timezone

from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Match(models.Model):
    date = models.DateTimeField(default=timezone.now())


class MatchDetail(models.Model):
    set_number = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, blank=False)
    match = models.ForeignKey(Match, on_delete=models.PROTECT, blank=False)

