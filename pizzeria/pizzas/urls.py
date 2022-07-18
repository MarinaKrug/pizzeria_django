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
    # path('v1/pizza_order', PizzaSelectionAPIVIEW.as_view(), name='all_pizzas'),
    path('v1/pizza_order', get_pizza, name='all_pizzas'),
    path('v1/pizza_order/<int:pizz_id>/', update_pizza, name='update_pizzas'),
    # path('v1/order', oredering_pizza, name='ordering_pizzas')
]

#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)