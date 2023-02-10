from rest_framework.decorators import api_view
from BdoWorldBossApi.Services.world_boss_service import WorldBossService

_service = WorldBossService()


@api_view(['GET', 'POST'])
def world_boss_list(request):
    if request.method == 'GET':
        return _service.get_all_world_bosses()

    elif request.method == 'POST':
        return _service.insert_world_boss(request.data)

@api_view(['GET', 'PUT', 'DELETE'])
def world_boss_detail(request, _id):
    if request.method == 'GET':
        return _service.get_world_boss_by_id(_id)

    elif request.method == 'PUT':
        return _service.update_world_boss(_id, request.data)

    else:
        return _service.delete_world_boss(_id)
