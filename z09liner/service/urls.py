from django.urls import path, include


# Views
from service.views import service_home, category_list, service_detail, my_service, service_delete, \
    service_create, search

from service.contractor.views import contractor, contractor_detail, contractor_create, contractor_category, \
    my_contract, contractor_search, contractor_redact


app_name = 'service'


urlpatterns = [
    path('', service_home, name='service_home'),
    path('category_list/<int:cate_pk>/', category_list, name='category_list'),
    path('service_detail/<int:srv_pk>/', service_detail, name='service_detail'),
    path('my_service/', my_service, name='my_service'),
    path('contractor_create/', contractor_create, name='contractor_create'),
    path('contractor/', contractor, name='contractor'),
    path('contractor_detail/<int:cont_pk>', contractor_detail, name='contractor_detail'),
    path('contractor_category/<int:cate_pk>', contractor_category, name='contractor_category'),
    path('my_contract/', my_contract, name='my_contract'),
    path('contractor_redact/', contractor_redact, name='contractor_redact'),

    path('service_delete/<int:srv_pk>/', service_delete, name='service_delete'),
    path('service_create/', service_create, name='service_create'),
    path('search/', search, name='search'),
    path('contractor_search/', contractor_search, name='contractor_search'),
]