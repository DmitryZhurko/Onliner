from django.shortcuts import render, redirect
import requests
from weather.forms import CityForm

APPID = "de7af1f8ea78a32642d002d65ca7d347"
URL_BASE = "http://api.openweathermap.org/data/2.5/"


def core_weather(request):
    q = "Minsk"
    lang = "RU"
    units = 'metric'
    appid = APPID
    data = requests.get(URL_BASE + "weather", params=locals()).json()
    temp = data['main']['temp']
    if temp > 0:
        core_temp = f'+{temp}'
    else:
        core_temp = f'-{temp}'
    return core_temp


def weather(request):
    if request.method == 'POST':
        city_form = CityForm(request.POST)
        if city_form.is_valid():
            q = city_form.cleaned_data['city']
    else:
        city_form = CityForm()
        q = "Minsk"
    lang = "RU"
    units = 'metric'
    appid = APPID
    cnt = 5
    data = requests.get(URL_BASE + "weather", params=locals()).json()
    data_forecast = requests.get(URL_BASE + "forecast", params=locals()).json()
    # current_weather
    description = list(map(lambda i: i['description'], data['weather']))[0]
    city = data['name']
    temp = data['main']['temp']
    wind = data['wind']['speed']
    pressure = int((data['main']['pressure']) * 0.75006375541921)
    humidity = data['main']['humidity']
    context = {'data': data, 'city_form': city_form, 'description': description, 'city': city,
               'temp': temp, 'wind': wind, 'pressure': pressure, 'humidity': humidity, 'data_forecast': data_forecast}
    return render(request, 'weather/weather.html', context)
