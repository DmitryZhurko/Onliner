from django.core.paginator import Paginator

from service.forms import RatingForm
from service.models import Category, Contractor, Rating


def contract_category(request):
    category = Category.objects.all()
    return category

