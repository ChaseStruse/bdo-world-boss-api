from response import Response
from rest_framework import serializers, status

from BdoWorldBossApi.Models.world_boss import WorldBoss
from BdoWorldBossApi import serializers

class WorldBossService():
    @staticmethod
    def get_all_world_bosses() -> Response:
        boss = WorldBoss.object.all()
        serializer = serializers.WorldBossSerializer(boss, many=True)
        return Response(serializer.data)

    @staticmethod
    def insert_world_boss(_data):
        serializer = serializers.WorldBossSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)