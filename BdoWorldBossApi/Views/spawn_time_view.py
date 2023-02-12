from rest_framework.decorators import api_view
from BdoWorldBossApi.Services.spawn_time_service import SpawnTimeService

_service = SpawnTimeService()


@api_view(['GET', 'POST'])
def spawn_time_list(request):
    if request.method == 'GET':
        return _service.get_all_spawn_times()

    elif request.method == 'POST':
        return _service.insert_spawn_time(request.data)


@api_view(['GET', 'PUT', 'DELETE'])
def spawn_time_detail(request, _id):
    if request.method == 'GET':
        return _service.get_spawn_time_by_id(_id)

    elif request.method == 'PUT':
        return _service.update_spawn_time(_id, request.data)

    else:
        return _service.delete_spawn_time(_id)

@api_view(['GET'])
def spawn_time_world_boss(request, _bossId):
    if request.method == 'GET':
        return _service.get_spawn_time_by_boss_id(_bossId)