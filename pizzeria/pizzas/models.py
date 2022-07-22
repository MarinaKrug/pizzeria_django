from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название пиццы", db_index=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=25, verbose_name="Наполнение пиццы")
    pizza = models.ForeignKey(Pizza, default=None, on_delete=models.CASCADE, verbose_name='название пиццы', blank=True)

    def __str__(self):
        return self.name

#
class PizzaOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id заказчика')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name='название пиццы')

    def __str__(self):
        return self.pizza


