from django.http import JsonResponse
from rest_framework import serializers, status
from BdoWorldBossApi.Models.spawn_times import SpawnTimes
from BdoWorldBossApi import serializers


class SpawnTimeService:
    @staticmethod
    def get_all_spawn_times():
        spawnTime = SpawnTimes.object.all()
        serializer = serializers.SpawnTimeSerializer(spawnTime, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def insert_spawn_time(_data):
        serializer = serializers.SpawnTimeSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

    def get_spawn_time_by_id(self, _id):
        spawnTime = self.__get_spawn_time_object_by_id(_id)
        serializer = serializers.SpawnTimeSerializer(spawnTime)
        return JsonResponse(serializer.data)

    def update_spawn_time(self, _id, _data):
        spawnTime = self.__get_spawn_time_object_by_id(_id)
        serializer = serializers.SpawnTimeSerializer(spawnTime, data=_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete_spawn_time(self, _id):
        spawnTime = self.__get_spawn_time_object_by_id(_id)
        spawnTime.delete()
        return JsonResponse(status.HTTP_204_NO_CONTENT, safe=False)

    def __get_spawn_time_object_by_id(self, _id: int) -> SpawnTimes:
        try:
            spawnTime = SpawnTimes.object.get(pk=_id)
            return spawnTime
        except:
            raise Exception(f'No spawn time found with id of {_id}')
