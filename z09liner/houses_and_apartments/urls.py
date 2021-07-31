from django.urls import path
from .views import flat_list, flat_detail, placing_a_sale, rent_list, place_a_lease, rent_detail, expensive, \
    cheap, by_date,  my_announcements, my_announcements_rent, \
    expensive_rent, cheap_rent, by_date_rent, flat_edit, rent_edit, rent_delete, flat_delete, by_apartment, by_flat, \
    by_apartment_rent, by_flat_rent, sorting_by_room, sorting_by_room_rent


app_name = 'houses_and_apartments'


urlpatterns = [
    path('', flat_list, name='flat_list'),
    path('rent_list/', rent_list, name='rent_list'),
    path('detail/<int:detail_pk>/', flat_detail, name='flat_detail'),
    path('rent_detail/<int:detail_pk>/', rent_detail, name='rent_detail'),
    path('placing_a_sale/', placing_a_sale, name='placing_a_sale'),
    path('place_a_lease/', place_a_lease, name='place_a_lease'),
    path('expensive/', expensive, name='expensive'),
    path('expensive_rent/', expensive_rent, name='expensive_rent'),
    path('cheap/', cheap, name='cheap'),
    path('cheap_rent/', cheap_rent, name='cheap_rent'),
    path('my_announcements/', my_announcements, name='my_announcements'),
    path('my_announcements_rent/', my_announcements_rent, name='my_announcements_rent'),
    path('by_date/', by_date, name='by_date'),
    path('by_date_rent/', by_date_rent, name='by_date_rent'),
    path('flat_edit/<int:edit_pk>/', flat_edit, name='flat_edit'),
    path('rent_edit/<int:rent_edit_pk>/', rent_edit, name='rent_edit'),
    path('rent_delete/<int:rent_delete_pk>/', rent_delete, name='rent_delete'),
    path('flat_delete/<int:flat_delete_pk>/', flat_delete, name='flat_delete'),
    path('by_apartment/', by_apartment, name='by_apartment'),
    path('by_apartment_rent/', by_apartment_rent, name='by_apartment_rent'),
    path('by_flat/', by_flat, name='by_flat'),
    path('by_flat/sorting_by_room/', sorting_by_room, name='sorting_by_room'),

    path('by_flat_rent/', by_flat_rent, name='by_flat_rent'),
    path('by_flat_rent/sorting_by_room_rent/', sorting_by_room_rent, name='sorting_by_room_rent'),
]
