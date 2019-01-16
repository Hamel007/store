from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Категории товаров
    """
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    slug = models.SlugField(max_length=100, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара
    """
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена", default=0)
    slug = models.SlugField(max_length=150)
    availability = models.BooleanField("Наличие", default=True)
    quantity = models.IntegerField("Количество", default=1)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class Cart(models.Model):
    """Корзина
    """
    customer = models.ForeignKey(User, verbose_name="Заказчик",
                                 on_delete=models.CASCADE)
    accepted = models.BooleanField("Заказ принят", default=False)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return "Корзина {}".format(self.customer)


class CartItem(models.Model):
    """Модель выбранных продуктов
    """
    purchase = models.ForeignKey(Product, verbose_name="Заказанный товар",
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField("Количество товара", default=0)
    cart = models.ForeignKey(Cart, verbose_name="Корзины",
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Заказанный товар"
        verbose_name_plural = "Заказанные товары"

    def __str__(self):
        return "Заказанный товар {}".format(self.purchase)


class Orders(models.Model):
    """Модель заказов
    """
    orders = models.ForeignKey(Cart, verbose_name="Заказы",
                               on_delete=models.CASCADE)
    done = models.BooleanField("Заказ выполнен", default=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "Заказ {}".format(self.orders.customer)



