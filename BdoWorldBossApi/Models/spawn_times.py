from django.db import models
from django.db.models import CASCADE

from BdoWorldBossApi.Models.world_boss import WorldBoss


class SpawnTimes(models.Model):
    day = models.CharField(max_length=20)
    time = models.TimeField()
    boss = models.ForeignKey(WorldBoss, on_delete=CASCADE)

    def __str__(self):
        return self.boss.name + ' ' + self.day
