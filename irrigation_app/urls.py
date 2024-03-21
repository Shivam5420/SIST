from django.urls import path,include
from . import views

urlpatterns = [
    path('api/sensor-data/', views.get_sensor_data, name='sensor_data'),
    path('api/weather-data/', views.get_weather_data, name='weather_data'),
    path('api/crop-list/', views.get_crop_list, name='crop_list'),
]
