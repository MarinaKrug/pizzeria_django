from django.contrib.auth.models import User
from rest_framework import serializers

from pizzas.models import Pizza, PizzaOrder


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = "__all__"





class PizzaOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # pizza = serializers.CharField(max_length=200)
    class Meta:
        model = PizzaOrder
        fields = "__all__"