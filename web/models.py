from django.db import models


# from django.contrib.auth.models import User


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class OrderStatus(models.TextChoices):
    PENDING = "PENDING", "pending"
    TRANSIT = "TRANSIT", "transit"
    DELIVERED = "DELIVERED", "delivered"


class Order(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    order_status = models.CharField(max_length=12, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    class Meta:
        db_table = "router"

    def __str__(self):
        return f'Order for {self.product.name} (Quantity: {self.count})'
