from django.urls import path, include

from rest_framework.routers import DefaultRouter

from service.api.api_views import CategoryView, CategoryDetailView, CommentView, CommentDetailView, ContractorView, \
    ContractorDetailView, UserView, UserDetailView, ServiceView, ServiceDetailView, CompareView

app_name = 'api'

router = DefaultRouter()

router.register('category', CategoryView, basename='CategoryView')
router.register('category/detail', CategoryDetailView, basename='CategoryDetailView')

router.register('service', ServiceView, basename='ServiceView')
router.register('service/detail', ServiceDetailView, basename='ServiceDetailView')

router.register('users', UserView, basename='UserView')
router.register('users/detail', UserDetailView, basename='UserDetailView')

router.register('contractor', ContractorView, basename='ContractorView')
router.register('contractor/detail', ContractorDetailView, basename='ContractorDetailView')

router.register('comment', CommentView, basename='CommentView')
router.register('comment/detail', CommentDetailView, basename='CommentDetailView')

router.register('compare', CompareView, basename='CompareView')






urlpatterns = [
    path('', include(router.urls))
]