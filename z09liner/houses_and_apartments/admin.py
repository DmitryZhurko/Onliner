from django.contrib import admin
from .models import SaleFlat, Photo, PhotoRent, Rent


admin.site.register(SaleFlat)
admin.site.register(Photo)

admin.site.register(Rent)
admin.site.register(PhotoRent)
