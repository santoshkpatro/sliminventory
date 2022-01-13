from django.db import models
from django.contrib.postgres import fields
from .base import BaseModel
from .warehouse import Warehouse
from .product import Product
from .supplier import Supplier


class Inventory(BaseModel):
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    images = fields.ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True
    )
    is_available = models.BooleanField(default=True)
    tags = fields.ArrayField(
        models.CharField(max_length=20),
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'inventories'
        unique_together = ['warehouse', 'product', 'supplier']

    def __str__(self) -> str:
        return self.name
