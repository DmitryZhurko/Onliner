from django.urls import path
from weather.views import weather

app_name = 'weather'

urlpatterns = [
    path('', weather, name='weather'),
]