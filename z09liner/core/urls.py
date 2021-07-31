from django.urls import path, include
from core.views import core_base

app_name = 'core'

urlpatterns = [
    path('', core_base, name='core_base'),
]

