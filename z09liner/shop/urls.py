from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import index, product_detail, shopping_cart, basket_add, basket_delete, checkout, user_orders


app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('<int:category_id>/', index, name='category'),
    path('page<int:page>/', index, name='page'),
    path('detail/<int:product_id>/', product_detail, name='product_detail'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_delete/<int:product_id>/', basket_delete, name='basket_delete'),
    path('checkout/', checkout, name='checkout'),
    # path('confirm_order/', confirm_order, name='confirm_order'),
    path('order_history/', user_orders, name='user_orders'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)