from django.shortcuts import render, redirect
from weather.views import core_weather
from currency.views import core_kurs_dollar


def core_base(request):
    return render(request, 'core/base.html', {'core_weather': core_weather(request),
                                              'kurs_dollar': core_kurs_dollar(request)})




