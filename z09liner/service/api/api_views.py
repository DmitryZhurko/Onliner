from rest_framework import mixins, viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from service.models import Category, Comment, Contractor, Service, Compare
from service.api.serializers import CategorySerializer, CommentSerializer, ContractorSerializer, UserSerializer, \
    ServiceSerializer, CompareSerializer
from users.models import User


# Category
class CategoryView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name']


class CategoryDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Comment
class CommentView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'text']


class CommentDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Contractor
class ContractorView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'first_name', 'last_name']


class ContractorDetailView(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


# User
class UserView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'username']


class UserDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Service
class ServiceView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'title', 'description', 'price']



class ServiceDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Сравнение
class CompareView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = Compare.objects.all()
    serializer_class = CompareSerializer

    def delete(self, request):
        compare = Compare.objects.all().delete()
        return Response(compare)
