from django.db import models
from django.contrib.postgres import fields
from .base import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    images = fields.ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    tags = fields.ArrayField(
        models.CharField(max_length=20),
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'products'

    def __str__(self) -> str:
        return self.name
