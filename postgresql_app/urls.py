from django.urls import path
from . import views

app_name = 'postgresql_app'

urlpatterns = [
    path('cars/get/', views.get_all_cars, name='get_all_cars'),
    path('cars/get/<int:car_id>/', views.get_car, name='get_car'),
    path('cars/create/', views.create_car, name='create_car'),
    path('cars/update/<int:car_id>/', views.update_car, name='update_car'),
    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),

    path('clients/get/', views.get_all_clients, name='get_all_clients'),
    path('clients/get/<int:client_id>/', views.get_client, name='get_client'),
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/update/<int:client_id>/', views.update_client, name='update_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),

    path('orders/get/', views.get_all_orders, name='get_all_orders'),
    path('orders/get/<int:order_id>/', views.get_order, name='get_order'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/update/<int:order_id>/', views.update_order, name='update_order'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),

]
