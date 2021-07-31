# Generated by Django 3.2.4 on 2021-07-13 14:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Категория')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='service.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500, verbose_name='О себе')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('user', models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category', verbose_name='Вид работ')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_active', models.DateField(blank=True, default='13.07.2021', null=True, verbose_name='Активно до')),
                ('status', models.CharField(choices=[('Активный', 'Активный'), ('Закрытый', 'Закрытый')], default='Активный', max_length=255, verbose_name='Статус')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Изображения')),
                ('category', models.ForeignKey(default='Разное', on_delete=django.db.models.deletion.CASCADE, to='service.category', verbose_name='Категория')),
                ('user', models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_cont', to='service.contractor', verbose_name='Исполнитель')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service')),
            ],
        ),
        migrations.CreateModel(
            name='CommentContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Ваше сообщение')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.contractor')),
                ('user', models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'ordering': ['date_create'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Ваше сообщение')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='service.comment')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service')),
                ('user', models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'ordering': ['date_create'],
            },
        ),
    ]
