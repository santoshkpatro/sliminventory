from django.db import models
from django.contrib.postgres import fields
from .base import BaseModel
from .warehouse import Warehouse
from .product import Product

class Inventory(BaseModel):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    images = fields.ArrayField(models.CharField(max_length=200), blank=True, null=True)
    is_available = models.BooleanField(default=True)
    tags = fields.ArrayField(models.CharField(max_length=20), blank=True, null=True)

    class Meta:
        db_table = 'inventories'
        unique_together = ['warehouse', 'product']

    def __str__(self) -> str:
        return self.name