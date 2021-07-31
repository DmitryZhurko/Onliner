from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('core.urls')),
    path('news/', include('news.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('users/', include('users.urls')),
    path('forum/', include('forum.urls')),
    path('weather/', include('weather.urls')),
    path('currency/', include('currency.urls')),
    path('shop/', include('shop.urls')),
    path('covid/', include('covid.urls')),
    path('search/', include('search.urls')),
    path('houses_and_apartments/', include('houses_and_apartments.urls')),
    path('service/', include('service.urls')),
    path('service/api/', include('service.api.urls')),
    path('used_cars/', include('used_cars.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    path('shop/', include('shop.urls')),

