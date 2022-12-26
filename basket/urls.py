from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_pg, name='basket_pg'),
    path('add/', views.basket_add, name='basket_add')
    
]