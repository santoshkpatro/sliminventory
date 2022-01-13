from django.db import models
from .base import BaseModel
from .user import User

class Warehouse(BaseModel):
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)
    is_operational = models.BooleanField(default=True)

    class Meta:
        db_table = 'warehouses'

    def __str__(self) -> str:
        return self.name