from django.urls import path
from django.conf.urls.static import static
from system import settings
from .views import used_cars_main_list, used_cars_ad, used_cars_main_list_category




urlpatterns = [
    path('', used_cars_main_list , name = 'used_cars_main_list'),
    path('category/<str:car_pk>', used_cars_main_list_category , name = 'used_cars_main_list_category'),
    path('<int:car_pk>', used_cars_ad , name = 'used_cars_ad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

