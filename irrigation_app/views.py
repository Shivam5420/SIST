from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData, WeatherData, Crop

def get_sensor_data(request):
    # Retrieve and return sensor data
    sensor_data = SensorData.objects.all()
    data = [{"timestamp": entry.timestamp, "depth": entry.depth, "moisture": entry.moisture, "temperature": entry.temperature} for entry in sensor_data]
    return JsonResponse(data, safe=False)

def get_weather_data(request):
    # Retrieve and return weather data
    weather_data = WeatherData.objects.all()
    data = [{"timestamp": entry.timestamp, "temperature": entry.temperature, "humidity": entry.humidity, "pressure": entry.pressure, "weather_description": entry.weather_description} for entry in weather_data]
    return JsonResponse(data, safe=False)

def get_crop_list(request):
    # Retrieve and return crop list
    crops = Crop.objects.all()
    crop_list = [{"name": crop.name, "water_needs": crop.water_needs} for crop in crops]
    return JsonResponse(crop_list, safe=False)
