# Python object -> Json serializer
from rest_framework import serializers
from BdoWorldBossApi.Models.world_boss import WorldBoss


class WorldBossSerializer(serializers.ModelSerializer):
    # Metadata
    class Meta:
        model = WorldBoss
        fields = ['id', 'name', 'region']