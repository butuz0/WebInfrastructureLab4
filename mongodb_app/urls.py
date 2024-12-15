from django.urls import path
from . import views

app_name = 'mongodb_app'

urlpatterns = [
    path('get/', views.get_all_sellers, name='get_all_sellers'),
    path('get/<int:seller_id>/', views.get_seller, name='get_seller'),
    path('create/', views.create_seller, name='create_seller'),
]
