from rest_framework.decorators import api_view
from BdoWorldBossApi.Services.world_boss_service import WorldBossService

_service = WorldBossService()


@api_view(['GET', 'POST'])
def world_boss_list(request):
    if request.method == 'GET':
        return _service.get_all_world_bosses()

    elif request.method == 'POST':
        return _service.insert_world_boss(request.data)