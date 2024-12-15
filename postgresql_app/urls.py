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
    path('clients/get/<int:client_id>/', views.get_client, name='get_clients'),
    path('clients/create/', views.create_client, name='create_clients'),
    path('clients/update/<int:client_id>/', views.update_client, name='update_clients'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_clients'),
]
