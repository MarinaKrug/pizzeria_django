from django.conf.urls.static import static
from django.urls import path
#
# from pizzeria import settings

"""Определяет схемы URL для pizzas"""

from .views import *


app_name = 'pizzas'


urlpatterns = [
    path('', index, name='home'),
    path('pizzas/', show_pizzas, name='list_pizzas'),
    path('pizzas/<int:pizza_id>', show_one_pizza, name='pizza'),
    path('api/v1/pizza_order', PizzasViewSet.as_view({"get": "list", "post": "create"}), name='all_pizzas'),
    path('api/v1/pizza_order/<int:pk>/', PizzasViewSet.as_view({"put": "partial_update"}), name='update_pizza'),
    path('api/v1/pizza_order_delete/<int:pk>/', PizzasViewSet.as_view({"delete": "destroy"}), name='delete_pizza'),
]

