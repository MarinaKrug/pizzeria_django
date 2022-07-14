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
    path('pizzas/<int:pizza_id>', show_one_pizza, name='pizza')
]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)