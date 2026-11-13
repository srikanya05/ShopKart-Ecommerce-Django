from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease'),
    path('remove/<int:item_id>/', views.remove_item, name='remove'),
    path('checkout/', views.checkout, name='checkout'),
]