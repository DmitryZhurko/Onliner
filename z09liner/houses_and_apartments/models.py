from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
from .filters import dollar


VARIANT = [
        ('Квартира', 'Квартира'),
        ('Дом', 'Дом')
    ]


class SaleFlat(models.Model):
    cost = models.PositiveIntegerField(verbose_name='стоимость квартиры')
    cost_dollar = models.FloatField(verbose_name='курс доллара', default=dollar)
    floor = models.PositiveIntegerField(verbose_name='этаж', default=1)
    total_area = models.DecimalField(verbose_name='общая площадь', max_digits=10, decimal_places=2)
    living_space = models.DecimalField(verbose_name='жилая площадь', max_digits=10, decimal_places=2)
    kitchen_area = models.DecimalField(verbose_name='площадь кухни', max_digits=10, decimal_places=2)
    ceiling_height = models.DecimalField(verbose_name='высота потолка', max_digits=10, decimal_places=2)
    number_of_rooms = models.PositiveIntegerField(verbose_name='количество комнат', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    description = models.TextField(verbose_name='описание')
    telephone = models.CharField(verbose_name='номер телефона', max_length=25)
    address = models.CharField(verbose_name='адрес', max_length=50)
    flat_or_apartment = models.CharField(verbose_name='дом или квартира', choices=VARIANT, max_length=35)

    def __str__(self):
        return f'{self.address}'


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='картинка', blank=True, null=True)
    saleflat = models.ForeignKey('SaleFlat', on_delete=models.CASCADE, related_name='photo')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name}, {self.id}'


class Rent(models.Model):
    cost = models.PositiveIntegerField(verbose_name='стоимость квартиры')
    cost_dollar = models.FloatField(verbose_name='курс доллара', default=dollar)
    floor = models.PositiveIntegerField(verbose_name='этаж', default=1)
    number_of_rooms = models.PositiveIntegerField(verbose_name='количество комнат', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    description = models.TextField(verbose_name='описание')
    telephone = models.CharField(verbose_name='номер телефона', max_length=25)
    address = models.CharField(verbose_name='адрес', max_length=50)
    tv = models.BooleanField(verbose_name='телевизор', default=False)
    furniture = models.BooleanField(verbose_name='мебель', default=False)
    plate = models.BooleanField(verbose_name='плита', default=False)
    refrigerator = models.BooleanField(verbose_name='холодильник', default=False)
    internet = models.BooleanField(verbose_name='интернет', default=False)
    conditioning = models.BooleanField(verbose_name='кондиционер', default=False)
    washer = models.BooleanField(verbose_name='стиральная машина', default=False)
    flat_or_apartment = models.CharField(verbose_name='дом или квартира', choices=VARIANT, max_length=35)

    def __str__(self):
        return f'{self.address}'


class PhotoRent(models.Model):
    image_rent = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='картинка', blank=True, null=True)
    rent = models.ForeignKey('Rent', on_delete=models.CASCADE, related_name='photo_rent')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name}, {self.id}'
