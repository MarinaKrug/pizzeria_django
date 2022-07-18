from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Пиццерия: создайте новый проект с именем pizzeria, содержащий приложение
# pizzas. Определите модель Pizza с полем name, в котором хранятся названия видов пиццы
# (например, «Гавайская» или «Четыре сыра»). Определите модель Topping с полями pizza
# и name. Поле pizza должно содержать внешний ключ к модели Pizza, а поле name должно
# позволять хранить такие значения, как «ананас» или «грибы».
# Зарегистрируйте обе модели на административном сайте. Используйте сайт для ввода названий пиццы и топпингов.
# Изучите введенные данные в интерактивной оболочке


class Pizza(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название пиццы", db_index=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=25, verbose_name="Наполнение пиццы")
    pizza = models.ManyToManyField(Pizza, verbose_name='название пиццы', blank=True)

    def __str__(self):
        return self.name


class PizzaOrder(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id заказчика')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name='название пиццы')
    topping = models.ManyToManyField(Topping, default=None, verbose_name='добавки')

