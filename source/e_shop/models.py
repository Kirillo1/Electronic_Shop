from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()

DEFAULT_CATEGORY = "other"
CATEGORY_CHOICES = [(DEFAULT_CATEGORY, 'другая'), ('monitors', 'мониторы'), ('processors', 'процессоры'),
                    ('keyboards', 'клавиатуры')]


def min_remainder_validator(value):
    if value < 0:
        raise ValidationError(f"Остаток не может быть меньше 0!")


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    description = models.CharField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    category = models.CharField(max_length=30, null=False, blank=False, verbose_name="Категория",
                                default=DEFAULT_CATEGORY,
                                choices=CATEGORY_CHOICES)
    remainder = models.PositiveIntegerField(verbose_name="Остаток", validators=(min_remainder_validator,))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.name}: {self.category}: {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ItemInCart(models.Model):
    product = models.ForeignKey("e_shop.Product", on_delete=models.CASCADE,
                                related_name="in_cart", verbose_name="Продукт")
    quantity = models.PositiveIntegerField(verbose_name="Колличество", default=1)

    def get_product_total(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    @classmethod
    def get_total(cls):
        total = 0
        for cart in cls.objects.all():
            total += cart.get_product_total()
        return total


class Order(models.Model):
    user_name = models.ForeignKey(User, related_name="orders", verbose_name="Имя", on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, verbose_name="Телефон", null=False, blank=False)
    address = models.CharField(max_length=100, verbose_name="Адрес", null=False, blank=False)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    products = models.ManyToManyField("e_shop.Product", related_name="orders", verbose_name="Продукты",
                                      through='e_shop.OrderProduct', through_fields=['order', 'product'])

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey('e_shop.Product', on_delete=models.CASCADE,
                                verbose_name='Продукт', related_name='order_product')
    order = models.ForeignKey('e_shop.Order', on_delete=models.CASCADE,
                              verbose_name='Заказ', related_name='order_product')
    quantity = models.PositiveIntegerField(verbose_name='Колличество')

    def __str__(self):
        return f'{self.product} - {self.quantity}'

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'
