from django.shortcuts import render
from .models import Used_cars_cars
# from .models import used_cars_list_status, used_cars_list_fuel, used_cars_list_transmission, used_cars_list_body


# used_cars_d = {'status': used_cars_list_status, 'fuel': used_cars_list_fuel, 'transmission': used_cars_list_transmission, 'body': used_cars_list_body, 'not_found': ''}




def used_cars_main_list(request):
    all = Used_cars_cars.objects.all()
    # used_cars_d['all']=all
    return render(request, 'used_cars_main_list.html')
    # return render(request, 'used_cars_main_list.html', used_cars_d)






def used_cars_main_list_category(request, car_pk):
    used_cars_l=[]
    not_found=''
    for i in Used_cars_cars.objects.all():
        if f'{i.status}' == car_pk:
            used_cars_l.append(i)
        elif f'{i.fuel}' ==car_pk:
            used_cars_l.append(i)
        elif f'{i.transmission}' ==car_pk:
            used_cars_l.append(i)
        elif f'{i.body}' ==car_pk:
            used_cars_l.append(i)
    if used_cars_l==[]:
        not_found='Ни чего не найдено :('
    used_cars_d['all']=used_cars_l
    used_cars_d['not_found'] = not_found
    return render(request, 'used_cars_main_list.html', used_cars_d)



def used_cars_ad(request, car_pk):
    car = Used_cars_cars.objects.get(pk=car_pk)
    used_cars_d['car'] = car
    return render(request, 'used_cars_ad.html', used_cars_d)


