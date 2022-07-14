from django.shortcuts import render

# Create your views here.
from pizzas.models import *


def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'pizzas/index.html')

def show_pizzas(request):
    """Страница для отображения списка всех пицц"""
    pizz = Pizza.objects.all()
    context = {'pizza': pizz}
    return render(request, 'pizzas/pizzas.html', context=context)

def show_one_pizza(request, pizza_id):
    """Выводит 1 пиццу и все ее дополнения"""
    pizza = Pizza.objects.get(pk=pizza_id)
    names = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'names': names}
    return render(request, 'pizzas/pizza.html', context=context)


