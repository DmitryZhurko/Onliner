from PIL.Image import Image
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from mptt.admin import MPTTModelAdmin

# Models
from service.models import Category, Service, Comment, Contractor, Rating, CommentContract


class RatingAdmin(admin.TabularInline):
    model = Rating


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_per_page = 30
    list_display = ['name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['user', 'category', 'title', 'date_create', 'price', 'status', 'image']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['user', 'service', 'text', 'date_create']



@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['user', 'work', 'phone']
    inlines = [RatingAdmin]


@admin.register(CommentContract)
class CommentContractAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['user', 'contractor', 'text', 'date_create']