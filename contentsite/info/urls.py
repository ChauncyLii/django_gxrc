from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    path('system/',views.system,name='system'),
    path('index/',views.index,name='index'),
    path('system/detail/<int:info_id>/',views.detail,name='detail')
]
