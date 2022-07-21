from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from pizzas.models import *
from pizzas.serializers import *
from pizzas.permissions import *

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


# class PizzasAPIList(generics.ListCreateAPIView):
#     queryset = Pizza.objects.all()
#     serializer_class = PizzaSerializer
#
# class PizzasAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Pizza.objects.all()
#     serializer_class = PizzaSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
# class PizzasAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Pizza.objects.all()
#     serializer_class = PizzaSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)



# class PizzasAPIList(generics.ListCreateAPIView):
#     queryset = PizzaOrder.objects.all()
#     serializer_class = PizzaOrderSerializer
#
# class PizzasAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PizzaOrder.objects.all()
#     serializer_class = PizzaOrderSerializer
#     permission_classes = (IsOwnerOrReadOnly,)




# class PizzasAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = PizzaOrder.objects.all()
#     serializer_class = PizzaOrderSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)


class PizzasViewSet(viewsets.ModelViewSet):
   queryset = PizzaOrder.objects.all()
   serializer_class = PizzaOrderSerializer
   permission_classes = (IsOwnerOrReadOnly,)


