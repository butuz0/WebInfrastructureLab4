from django.urls import path
from . import views

app_name = 'postgresql_app'

urlpatterns = [
    path('cars/get/', views.get_all_cars, name='get_all_cars'),
    path('cars/get/<int:car_id>/', views.get_car, name='get_car'),
    path('cars/create/', views.create_car, name='create_car'),
    path('cars/update/<int:car_id>/', views.update_car, name='update_car'),
    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),

]
