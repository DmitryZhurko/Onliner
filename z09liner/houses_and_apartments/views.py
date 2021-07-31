from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from .models import SaleFlat, Photo, Rent, PhotoRent
from .forms import FullFlatForm, FullRentForm
from django.core.paginator import Paginator
from .filters import dollar, foo_paginator, sessions, sort, filter_number_of_rooms


def flat_list(request):
    my_session = sessions(request)
    count = SaleFlat.objects.all().count()
    all_flat = foo_paginator(request, SaleFlat.objects.all(), 5)
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar, 'var': my_session})


def flat_detail(request, detail_pk):
    flat = SaleFlat.objects.filter(pk=detail_pk).first()
    photo_flat = flat.photo.all()
    return render(request, 'houses_and_apartments/flat_detail.html', {'flat': flat, 'photo_flat': photo_flat})


def placing_a_sale(request):
    error = ''
    if request.method == 'POST':
        flatform = FullFlatForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if flatform.is_valid():
            user = request.user
            cost = flatform.cleaned_data['cost']
            cost_dollar = int(cost/flatform.cleaned_data['cost_dollar'])
            floor = flatform.cleaned_data['floor']
            total_area = flatform.cleaned_data['total_area']
            living_space = flatform.cleaned_data['living_space']
            kitchen_area = flatform.cleaned_data['kitchen_area']
            ceiling_height = flatform.cleaned_data['ceiling_height']
            number_of_rooms = flatform.cleaned_data['number_of_rooms']
            description = flatform.cleaned_data['description']
            telephone = flatform.cleaned_data['telephone']
            address = flatform.cleaned_data['address']
            flat_or_apartment = flatform.cleaned_data['flat_or_apartment']
            flat_obj = SaleFlat.objects.create(user=user, cost=cost, floor=floor, total_area=total_area,
                                               living_space=living_space, kitchen_area=kitchen_area,
                                               ceiling_height=ceiling_height, number_of_rooms=number_of_rooms,
                                               description=description, telephone=telephone,
                                               address=address, cost_dollar=cost_dollar, flat_or_apartment=flat_or_apartment)
            for i in files:
                Photo.objects.create(user=user, saleflat=flat_obj, image=i)
            return redirect('houses_and_apartments:flat_detail', detail_pk=flat_obj.pk)

        else:
            error = 'Форма не валидна!!!'
    photoform = FullFlatForm()
    return render(request, 'houses_and_apartments/placing_a_sale.html', {'photoform': photoform, 'error': error})


def rent_list(request):
    my_session = sessions(request)
    count = Rent.objects.all().count()
    all_flat = foo_paginator(request, Rent.objects.all(), 5)
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar, 'var': my_session})


def place_a_lease(request):
    error = ''
    if request.method == 'POST':
        fullrentform = FullRentForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('photos')
        if fullrentform.is_valid():
            user = request.user
            cost = fullrentform.cleaned_data['cost']
            cost_dollar = int(cost / fullrentform.cleaned_data['cost_dollar'])
            floor = fullrentform.cleaned_data['floor']
            number_of_rooms = fullrentform.cleaned_data['number_of_rooms']
            description = fullrentform.cleaned_data['description']
            telephone = fullrentform.cleaned_data['telephone']
            address = fullrentform.cleaned_data['address']
            tv = fullrentform.cleaned_data['tv']
            furniture = fullrentform.cleaned_data['furniture']
            plate = fullrentform.cleaned_data['plate']
            refrigerator = fullrentform.cleaned_data['refrigerator']
            internet = fullrentform.cleaned_data['internet']
            conditioning = fullrentform.cleaned_data['conditioning']
            washer = fullrentform.cleaned_data['washer']
            flat_or_apartment = fullrentform.cleaned_data['flat_or_apartment']
            rent_obj = Rent.objects.create(user=user, cost=cost, floor=floor, number_of_rooms=number_of_rooms,
                                               description=description, telephone=telephone,
                                               address=address, tv=tv, furniture=furniture, plate=plate, refrigerator=refrigerator,
                                           internet=internet, conditioning=conditioning, washer=washer, cost_dollar=cost_dollar, flat_or_apartment=flat_or_apartment)
            for r in files:
                PhotoRent.objects.create(user=user, rent=rent_obj, image_rent=r)
            return redirect('houses_and_apartments:rent_detail', detail_pk=rent_obj.pk)

        else:
            error = 'Форма не валидна!!!'
    fullrentform = FullRentForm()
    return render(request, 'houses_and_apartments/place_a_lease.html', {'fullrentform': fullrentform, 'error': error})


def rent_detail(request, detail_pk):
    rent = Rent.objects.filter(pk=detail_pk).first()
    photo_rent = rent.photo_rent.all()
    return render(request, 'houses_and_apartments/rent_detail.html', {'rent': rent, 'photo_rent': photo_rent})


def expensive(request):
    sorts = sort(request, queryset=SaleFlat, order='-cost')
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': sorts[0], 'count': sorts[1], 'dollar': dollar})


def expensive_rent(request):
    sorts = sort(request, queryset=Rent, order='-cost')
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': sorts[0], 'count': sorts[1], 'dollar': dollar})


def cheap(request):
    sorts = sort(request, queryset=SaleFlat, order='cost')
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': sorts[0], 'count': sorts[1], 'dollar': dollar})


def cheap_rent(request):
    sorts = sort(request, queryset=Rent, order='cost')
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': sorts[0], 'count': sorts[1], 'dollar': dollar})


def by_date(request):
    sorts = sort(request, queryset=SaleFlat, order='-date')
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': sorts[0], 'count': sorts[1], 'dollar': dollar})


def by_date_rent(request):
    sorts = sort(request, queryset=Rent, order='-date')
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': sorts[0], 'count': sorts[1], 'dollar': dollar})


def by_apartment(request):
    my_session = sessions(request)
    count = SaleFlat.objects.filter(flat_or_apartment='Дом').count()
    all_flat = foo_paginator(request, SaleFlat.objects.filter(flat_or_apartment='Дом'), 5)
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar, 'var': my_session})


def by_apartment_rent(request):
    my_session = sessions(request)
    count = Rent.objects.filter(flat_or_apartment='Дом').count()
    all_flat = foo_paginator(request, Rent.objects.filter(flat_or_apartment='Дом'), 5)
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar, 'var': my_session})


def by_flat(request):
    my_session = sessions(request)
    count = SaleFlat.objects.filter(flat_or_apartment='Квартира').count()
    all_flat = foo_paginator(request, SaleFlat.objects.filter(flat_or_apartment='Квартира'), 5)
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar, 'var': my_session})


def sorting_by_room(request):
    filter_rooms = filter_number_of_rooms(request, SaleFlat)
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': filter_rooms[1], 'count': filter_rooms[0], 'dollar': dollar})


def sorting_by_room_rent(request):
    filter_rooms = filter_number_of_rooms(request, Rent)
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': filter_rooms[1], 'count': filter_rooms[0], 'dollar': dollar})


def by_flat_rent(request):
    my_session = sessions(request)
    count = Rent.objects.filter(flat_or_apartment='Квартира').count()
    all_flat = foo_paginator(request, Rent.objects.filter(flat_or_apartment='Квартира'), 5)
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar, 'var': my_session})


def my_announcements(request):
    all_flat = SaleFlat.objects.filter(user=request.user)
    count = all_flat.count()
    all_flat = foo_paginator(request, all_flat, 5)
    return render(request, 'houses_and_apartments/flat_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar})


def my_announcements_rent(request):
    all_flat = Rent.objects.filter(user=request.user)
    count = all_flat.count()
    all_flat = foo_paginator(request, all_flat, 5)
    return render(request, 'houses_and_apartments/rent_list.html', {'all_flat': all_flat, 'count': count, 'dollar': dollar})


def flat_edit(request, edit_pk):
    error = ''
    flats = SaleFlat.objects.filter(pk=edit_pk).first()
    if request.method == 'GET':
        photoform = FullFlatForm(instance=flats)
        return render(request, 'houses_and_apartments/placing_a_sale.html', {'photoform': photoform, 'error': error})
    else:
        flatform = FullFlatForm(request.POST, request.FILES, instance=flats)
        files = request.FILES.getlist('images')
        if flatform.is_valid():
            flatform.save()
            user = request.user
            cost = flatform.cleaned_data['cost']
            cost_dollar = int(cost / flatform.cleaned_data['cost_dollar'])
            floor = flatform.cleaned_data['floor']
            total_area = flatform.cleaned_data['total_area']
            living_space = flatform.cleaned_data['living_space']
            kitchen_area = flatform.cleaned_data['kitchen_area']
            ceiling_height = flatform.cleaned_data['ceiling_height']
            number_of_rooms = flatform.cleaned_data['number_of_rooms']
            description = flatform.cleaned_data['description']
            telephone = flatform.cleaned_data['telephone']
            address = flatform.cleaned_data['address']
            flat_or_apartment = flatform.cleaned_data['flat_or_apartment']
            flat_obj = SaleFlat.objects.create(user=user, cost=cost, floor=floor, total_area=total_area,
                                               living_space=living_space, kitchen_area=kitchen_area,
                                               ceiling_height=ceiling_height, number_of_rooms=number_of_rooms,
                                               description=description, telephone=telephone,
                                               address=address, flat_or_apartment=flat_or_apartment, cost_dollar=cost_dollar)
            for i in files:
                Photo.objects.create(user=user, saleflat=flat_obj, image=i)
            flats.delete()
            return redirect('houses_and_apartments:flat_detail', detail_pk=flat_obj.pk)

        else:
            error = 'Форма не валидна!!!'


def rent_edit(request, rent_edit_pk):
    error = ''
    rents = Rent.objects.filter(pk=rent_edit_pk).first()
    if request.method == 'GET':
        fullrentform = FullRentForm(instance=rents)
        return render(request, 'houses_and_apartments/place_a_lease.html', {'fullrentform': fullrentform, 'error': error})
    else:
        fullrentform = FullRentForm(request.POST, request.FILES, instance=rents)
        files = request.FILES.getlist('photos')
        if fullrentform.is_valid():
            fullrentform.save()
            user = request.user
            cost = fullrentform.cleaned_data['cost']
            cost_dollar = int(cost / FullRentForm.cleaned_data['cost_dollar'])
            floor = fullrentform.cleaned_data['floor']
            number_of_rooms = fullrentform.cleaned_data['number_of_rooms']
            description = fullrentform.cleaned_data['description']
            telephone = fullrentform.cleaned_data['telephone']
            address = fullrentform.cleaned_data['address']
            tv = fullrentform.cleaned_data['tv']
            furniture = fullrentform.cleaned_data['furniture']
            plate = fullrentform.cleaned_data['plate']
            refrigerator = fullrentform.cleaned_data['refrigerator']
            internet = fullrentform.cleaned_data['internet']
            conditioning = fullrentform.cleaned_data['conditioning']
            washer = fullrentform.cleaned_data['washer']
            flat_or_apartment = fullrentform.cleaned_data['flat_or_apartment']
            rent_obj = Rent.objects.create(user=user, cost=cost, floor=floor, number_of_rooms=number_of_rooms,
                                           description=description, telephone=telephone,
                                           address=address, tv=tv, furniture=furniture, plate=plate,
                                           refrigerator=refrigerator,
                                           internet=internet, conditioning=conditioning, washer=washer, cost_dollar=cost_dollar,
                                           flat_or_apartment=flat_or_apartment)
            for i in files:
                PhotoRent.objects.create(user=user, rent=rent_obj, image_rent=i)
            rents.delete()
            return redirect('houses_and_apartments:rent_detail', detail_pk=rent_obj.pk)

        else:
            error = 'Форма не валидна!!!'


def rent_delete(request, rent_delete_pk):
    rents = Rent.objects.filter(pk=rent_delete_pk).delete()
    return redirect('houses_and_apartments:rent_list')


def flat_delete(request, flat_delete_pk):
    rents = SaleFlat.objects.filter(pk=flat_delete_pk).delete()
    return redirect('houses_and_apartments:flat_list')
