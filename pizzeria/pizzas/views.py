from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from pizzas.models import *
from pizzas.serializers import *

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


def get_pizza(request):

    if request.method == 'GET':
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def update_pizza(request, pizz_id):
    try:
        pizzas = Pizza.objects.get(pk=pizz_id)
    except Pizza.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'UPDATE':
        if request.user.is_authenticated:
            data = JSONParser().parse(request)
            serializer = PizzaSerializer(Pizza, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if request.user.is_authenticated:
            pizzas.delete()
            return HttpResponse(status=204)




# class GetPizzas(generics.ListCreateAPIView):
#     queryset = Pizza.objects.all()
#     serializer_class = serializers.PizzaSerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
