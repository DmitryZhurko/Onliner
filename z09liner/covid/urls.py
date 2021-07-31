from django.urls import path
from covid.views import covid

app_name = 'covid'

urlpatterns = [
    path('', covid, name='covid'),
]