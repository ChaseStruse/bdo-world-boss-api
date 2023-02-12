from django.contrib import admin
from django.urls import path
from BdoWorldBossApi.Views import world_boss_view, spawn_time_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worldboss/', world_boss_view.world_boss_list),
    path('worldboss/<int:_id>', world_boss_view.world_boss_detail),
    path('spawntime/', spawn_time_view.spawn_time_list),
    path('spawntime/<int:_id>', spawn_time_view.spawn_time_detail),
    path('spawntime/worldboss/<int:_bossId>', spawn_time_view.spawn_time_world_boss)
]
