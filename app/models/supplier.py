from django.db import models
from .base import BaseModel


class Supplier(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'suppliers'

    def __str__(self) -> str:
        return self.name
