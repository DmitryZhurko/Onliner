from django.urls import path
from currency.views import currency

app_name = 'currency'

urlpatterns = [
    path('', currency, name='currency'),
]