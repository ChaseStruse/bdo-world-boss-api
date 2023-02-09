from django.contrib import admin

from BdoWorldBossApi.Models.spawn_times import SpawnTimes
from BdoWorldBossApi.Models.world_boss import WorldBoss

admin.site.register(WorldBoss)
admin.site.register(SpawnTimes)
