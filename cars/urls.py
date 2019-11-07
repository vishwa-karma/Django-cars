from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name="car_detail"),
    path('car/new', views.new_car, name='new_car'),
    path('car/<int:pk>/edit/', views.car_edit, name='car_edit'),
    #path('car/<int:pk>/delete/', views.car_delete, name='car_delete'),
]