from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ClientViewSet, OrderViewSet

app_name = 'postgresql_app'

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
