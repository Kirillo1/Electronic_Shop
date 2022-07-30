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
