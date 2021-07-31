from django.core.paginator import Paginator

from service.models import Category, Comment, Service, Contractor

from service.filters import ServiceFilter



# Paginator - счетчик страниц
def paginator(request, name):

    paginator = Paginator(name, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


# Filter - сортирока
def my_filter(request, name):
    my_filter = ServiceFilter(request.GET, queryset=name)
    return my_filter


# Рефактор
def get_page_obj( request,  obj):
    my_filters = my_filter(request, obj)
    service = my_filters.qs

    page_obj = paginator(request, service)
    return page_obj, my_filters


def view_mixin(request, cate_pk, queryset):
    category = Category.objects.all()

    order_filter = request.GET.get('param') or '-date_create'
    service = queryset.order_by(f'{order_filter}')

    page_obj = get_page_obj(request, service)
    return category, page_obj
