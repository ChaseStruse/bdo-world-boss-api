from django.contrib import admin
from django.urls import path
from BdoWorldBossApi.Views import world_boss_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worldboss/', world_boss_view.world_boss_list),
    path('worldboss/<int:_id>', world_boss_view.world_boss_detail)
]
