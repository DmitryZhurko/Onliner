import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator

URL = "https://www.nbrb.by/statistics/rates/ratesdaily.asp"
page_text = requests.get(URL).text
soup = BeautifulSoup(page_text, 'html.parser')
link = soup.find_all('td', {'class': 'curCours'})
a = link[5].text.replace('\n', '')
dollar = float(a.replace(',', '.'))


def foo_paginator(request, object, count=5):
    paginator = Paginator(object, count)
    num_page = request.GET.get('page')
    all_flat = paginator.get_page(num_page)
    return all_flat


def sessions(request):
    var = request.GET.get('param')
    request.session['var'] = var
    request.session['number_of_rooms'] = var
    return var


def sort(request, queryset, order):
    if request.session['number_of_rooms'] == '4' and request.session['var'] == 'Квартира':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms__gte=4).order_by(order)
    elif request.session['number_of_rooms'] == '1' and request.session['var'] == 'Квартира':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms=request.session['number_of_rooms']).order_by(order)
    elif request.session['number_of_rooms'] == '2' and request.session['var'] == 'Квартира':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms=request.session['number_of_rooms']).order_by(order)
    elif request.session['number_of_rooms'] == '3' and request.session['var'] == 'Квартира':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms=request.session['number_of_rooms']).order_by(order)

    elif request.session['number_of_rooms'] == '4' and request.session['var'] == 'Дом':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms__gte=4).order_by(order)
    elif request.session['number_of_rooms'] == '1' and request.session['var'] == 'Дом':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms=request.session['number_of_rooms']).order_by(order)
    elif request.session['number_of_rooms'] == '2' and request.session['var'] == 'Дом':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms=request.session['number_of_rooms']).order_by(order)
    elif request.session['number_of_rooms'] == '3' and request.session['var'] == 'Дом':
        all_flat = queryset.objects.filter(flat_or_apartment=request.session['var'], number_of_rooms=request.session['number_of_rooms']).order_by(order)

    elif request.session['var'] == 'Квартира' and request.session['number_of_rooms'] == 'zero':
        all_flat = queryset.objects.filter(flat_or_apartment='Квартира').order_by(order)
    elif request.session['var'] and request.session['number_of_rooms'] == 'zero' == 'Дом':
        all_flat = queryset.objects.filter(flat_or_apartment='Дом').order_by(order)
    elif request.session['var'] == 'zero' and request.session['number_of_rooms'] == 'zero':
        all_flat = queryset.objects.all().order_by(order)
    count = all_flat.count()
    all_flat = foo_paginator(request, all_flat, 5)
    return all_flat, count


def filter_number_of_rooms(request, queryset):
    number = request.GET.get('param')
    my_type = request.session['var']
    request.session['number_of_rooms'] = number
    if number == '4':
        count = queryset.objects.filter(flat_or_apartment=my_type, number_of_rooms__gte=4).count()
        all_flat = foo_paginator(request, queryset.objects.filter(flat_or_apartment=my_type, number_of_rooms__gte=4), 5)
    else:
        count = queryset.objects.filter(flat_or_apartment=my_type, number_of_rooms=int(number)).count()
        all_flat = foo_paginator(request, queryset.objects.filter(flat_or_apartment=my_type, number_of_rooms=int(number)), 5)
    return count, all_flat