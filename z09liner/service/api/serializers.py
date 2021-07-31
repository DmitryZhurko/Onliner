
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from service.models import Category, Comment, Contractor, Service, User, Compare



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    service_title = serializers.ReadOnlyField(source='service.title')
    service = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ['user', 'user_name', 'text', 'service', 'service_title']


class ContractorSerializer(serializers.ModelSerializer):

    work_name = serializers.ReadOnlyField(source='work.name')
    user_username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Contractor
        fields = ['id', 'user', 'user_username', 'first_name', 'last_name', 'description', 'phone', 'work', 'work_name']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']


class ServiceSerializer(serializers.ModelSerializer):

    category_name = serializers.ReadOnlyField(source='category.name')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Service
        fields = ['id', 'user', 'user_name', 'category', 'category_name', 'title', 'description', 'price',
                  'address', 'date_create', 'date_active', 'status']


class CompareSerializer(serializers.ModelSerializer):

    service_name = serializers.ReadOnlyField(source='service.title')
    service_category = serializers.ReadOnlyField(source='service.category.name')
    service_price = serializers.ReadOnlyField(source='service.price')
    service_address = serializers.ReadOnlyField(source='service.address')
    service_date_create = serializers.ReadOnlyField(source='service.date_create')
    service_date_active = serializers.ReadOnlyField(source='service.date_active')
    service_status = serializers.ReadOnlyField(source='service.status')

    class Meta:
        model = Compare
        fields = ['service', 'service_name', 'service_category', 'service_price', 'service_address',
                  'service_date_create', 'service_date_active', 'service_status']

    def create(self, validated_data):
        return Compare.objects.create(**validated_data)


