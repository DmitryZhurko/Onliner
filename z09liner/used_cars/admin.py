from django.contrib import admin
from .models import Used_cars_cars, Used_cars_cart, Used_cars_fuel, Used_cars_color, Used_cars_transmission, Used_cars_status, Used_cars_body, Used_cars_type_of_drive

admin.site.register(Used_cars_cars)
admin.site.register(Used_cars_cart)


# admin.site.register(Used_cars_fuel)
# admin.site.register(Used_cars_color)
# admin.site.register(Used_cars_transmission)
# admin.site.register(Used_cars_status)
# admin.site.register(Used_cars_body)
# admin.site.register(Used_cars_type_of_drive)