from django.db import models


class WorldBoss(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    object = models.Manager()

    def __str__(self):
        return self.name