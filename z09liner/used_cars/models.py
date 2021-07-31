from django.db import models
from django.contrib.auth.models import User


class Used_cars_color(models.Model):
    color = models.CharField(max_length=30, verbose_name='Цвет')

    def __str__(self):
        return f'{self.color}'


class Used_cars_fuel(models.Model):
    fuel = models.CharField(max_length=30, verbose_name='Тип топлива')

    def __str__(self):
        return f'{self.fuel}'

class Used_cars_transmission(models.Model):
    transmission = models.CharField(max_length=30, verbose_name='Коробка')

    def __str__(self):
        return f'{self.transmission}'


class Used_cars_body(models.Model):
    body = models.CharField(max_length=30, verbose_name='Кузов')

    def __str__(self):
        return f'{self.body}'



class Used_cars_type_of_drive(models.Model):
    type_of_drive = models.CharField(max_length=30, verbose_name='Привод')

    def __str__(self):
        return f'{self.type_of_drive}'


class Used_cars_status(models.Model):
    status = models.CharField(max_length=30, verbose_name='Состояние')

    def __str__(self):
        return f'{self.status}'





# used_cars_list_colors = ['Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Голубой', 'Синий',  'Фиолетовый', 'Черный', 'Белый', 'Серый',]
# for i in used_cars_list_colors:
#     if Used_cars_color.objects.filter(color=i).first()==None:
#         Used_cars_color(color = i).save()
#
#
#
# used_cars_list_fuel = ['Бензин', 'Дизель', 'Электро',]
# for i in used_cars_list_fuel:
#     if Used_cars_fuel.objects.filter(fuel=i).first()==None:
#         Used_cars_fuel(fuel = i).save()
#
#
#
# used_cars_list_transmission = ['Автоматическая', 'Механическая',]
# for i in used_cars_list_transmission:
#     if Used_cars_transmission.objects.filter(transmission=i).first()==None:
#         Used_cars_transmission(transmission = i).save()
#
#
#
# used_cars_list_body = ['Седан', 'Внедорожник', 'Универсал', 'Хетчбэк', 'Лифтбэк', 'Минивэн', 'Микроавтобус', 'Купе', 'Фургон', 'Пикап', 'Кабриолет', 'Лимузин',]
# for i in used_cars_list_body:
#     if Used_cars_body.objects.filter(body=i).first()==None:
#         Used_cars_body(body = i).save()
#
#
#
# used_cars_list_type_of_drive = ['Передний', 'Задний', 'Полный',]
# for i in used_cars_list_type_of_drive:
#     if Used_cars_type_of_drive.objects.filter(type_of_drive=i).first()==None:
#         Used_cars_type_of_drive(type_of_drive = i).save()
#
#
#
# used_cars_list_status = ['Новый', 'С пробегом', 'Аварийный',]
# for i in used_cars_list_status:
#     if Used_cars_status.objects.filter(status=i).first()==None:
#         Used_cars_status(status = i).save()






class Used_cars_cars(models.Model):
    name_car = models.CharField(max_length=50, verbose_name= 'Название авто')
    text = models.TextField(verbose_name='Описание')
    color = models.ForeignKey(Used_cars_color, on_delete=models.CASCADE, verbose_name='Цвет')
    engine_volume = models.FloatField(verbose_name= 'Обьем двигателя (л)')
    fuel = models.ForeignKey(Used_cars_fuel, on_delete=models.CASCADE, verbose_name= 'Тип двигателя')
    transmission = models.ForeignKey(Used_cars_transmission, on_delete=models.CASCADE, verbose_name= 'Коробка')
    body = models.ForeignKey(Used_cars_body, on_delete=models.CASCADE, verbose_name= 'Кузов')
    power = models.IntegerField(verbose_name= 'Мощность (л.с)')
    type_of_drive = models.ForeignKey(Used_cars_type_of_drive, on_delete=models.CASCADE, verbose_name= 'Привод')
    mileage = models.IntegerField(verbose_name= 'Пробег (км)')
    status = models.ForeignKey(Used_cars_status, on_delete=models.CASCADE, verbose_name= 'Состояние')
    year = models.IntegerField(verbose_name= 'Год выпуска')
    city = models.CharField(max_length=20, verbose_name= 'Местонахождение/город')
    prise = models.FloatField(verbose_name= 'Цена (BYN)')
    created_date = models.DateTimeField(verbose_name='Дата создания')
    publish_date = models.DateTimeField(verbose_name='Дата публикации', blank=False)
    photo1 = models.ImageField(upload_to='used_cars')
    photo2 = models.ImageField(upload_to='used_cars')
    photo3 = models.ImageField(upload_to='used_cars')
    def __str__(self):
        return f'{self.name_car}'




class Used_cars_cart(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('Used_cars_cars', related_name='Продукты')

    def __str__(self):
        return f'{self.user}'