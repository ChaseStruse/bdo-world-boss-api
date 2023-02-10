# Python object -> Json serializer
from rest_framework import serializers

from BdoWorldBossApi.Models.spawn_times import SpawnTimes
from BdoWorldBossApi.Models.world_boss import WorldBoss


class WorldBossSerializer(serializers.ModelSerializer):
    # Metadata
    class Meta:
        model = WorldBoss
        fields = ['id', 'name', 'region']


class SpawnTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpawnTimes
        fields = ['id', 'day', 'time', 'boss']