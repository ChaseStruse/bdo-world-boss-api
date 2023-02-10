from django.http import JsonResponse
from rest_framework import serializers, status
from BdoWorldBossApi.Models.world_boss import WorldBoss
from BdoWorldBossApi import serializers


class WorldBossService:
    @staticmethod
    def get_all_world_bosses():
        boss = WorldBoss.object.all()
        serializer = serializers.WorldBossSerializer(boss, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def insert_world_boss(_data):
        serializer = serializers.WorldBossSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

    def get_world_boss_by_id(self, _id):
        boss = self.__get_world_boss_object_by_id(_id)
        serializer = serializers.WorldBossSerializer(boss)
        return JsonResponse(serializer.data)

    def update_world_boss(self, _id, _data):
        boss = self.__get_world_boss_object_by_id(_id)
        serializer = serializers.WorldBossSerializer(boss, data=_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete_world_boss(self, _id):
        boss = self.__get_world_boss_object_by_id(_id)
        boss.delete()
        return JsonResponse(status.HTTP_204_NO_CONTENT, safe=False)

    def __get_world_boss_object_by_id(self, _id: int) -> WorldBoss:
        try:
            boss = WorldBoss.object.get(pk=_id)
            return boss
        except:
            raise Exception(f'No world boss found with id of {_id}')
