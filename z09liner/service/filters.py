import django_filters

from service.models import Category, Service, Comment, Contractor



class ServiceFilter(django_filters.FilterSet):
    class Meta:

        model = Service

        fields = ['status']

