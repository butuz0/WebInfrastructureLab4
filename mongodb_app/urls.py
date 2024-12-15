from django.urls import path, include
from . import views
from .views import SellerViewSet
from rest_framework.routers import DefaultRouter

app_name = 'mongodb_app'

router = DefaultRouter()
router.register(r'sellers', SellerViewSet, basename='seller')

urlpatterns = [
    path('', include(router.urls)),
]
