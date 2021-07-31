import sys


from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MinValueValidator, MaxValueValidator
from six import BytesIO

from users.models import User
from django.db import models
import datetime


from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    name = models.CharField(max_length=255, unique=True, verbose_name='Категория')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):

    STATUS = (('Активный', 'Активный'), ('Закрытый', 'Закрытый'))

    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (1200, 1200)
    MAX_IMAGE_SIZE = 3145728

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name='Пользователь')

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, verbose_name='Цена')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_active = models.DateField(default=datetime.datetime.today().strftime('%d.%m.%Y'), blank=True, null=True, verbose_name='Активно до')
    status = models.CharField(max_length=255, choices=STATUS, default='Активный', verbose_name='Статус')
    image = models.ImageField(upload_to='img', null=True, blank=True, verbose_name='Изображения')

    def __str__(self):
        return f'{self.title}'

    # Изменение размера картинки
    def save(self, *args, **kwargs):
        super().save()

        # Open image using self
        img = Image.open(self.image.path)

        # saving image at the same path
        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)


class Comment(models.Model):

    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name='Пользователь')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    text = models.TextField(max_length=1000, verbose_name='Ваше сообщение')
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_create']

    def __str__(self):
        return f'{self.text}'


class Contractor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name='Пользователь')
    description = models.TextField(max_length=500, verbose_name='О себе')
    work = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Вид работ')
    phone = models.CharField(max_length=25, verbose_name='Телефон')

    def get_average_review_score(self):
        average_score = 0.0
        if self.rating_cont.count() > 0:
            total_score = sum([rating_product.rating for rating_product in self.rating_cont.all()])
            average_score = total_score / self.rating_cont.count()
        return round(average_score, 1)

    def __str__(self):
        return f'{self.user}, {self.phone}'


class Rating(models.Model):

    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name='Исполнитель',
                                   related_name='rating_cont')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}'


class CommentContract(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name='Пользователь')
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, verbose_name='Ваше сообщение')
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_create']

    def __str__(self):
        return f'{self.text}'


# API
class Compare(models.Model):

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.service}'