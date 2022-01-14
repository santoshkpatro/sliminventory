from django.db import IntegrityError
from rest_framework import generics, serializers
from app.models import Inventory
from app.models import Warehouse, Supplier, Product
from app.exceptions.warehouse import WarehouseNotFoundException
from app.exceptions.supplier import SupplierNotFoundException
from app.exceptions.product import ProductNotFoundException
from app.exceptions.inventory import UniqueInventoryException


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'capacity', 'location']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'price']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'location']


class InventorySerializer(serializers.ModelSerializer):
    warehouse_id = serializers.IntegerField(write_only=True, required=False)
    product_id = serializers.IntegerField(write_only=True, required=False)
    supplier_id = serializers.IntegerField(write_only=True, required=False)

    warehouse = WarehouseSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = [
            'id',
            'uuid',
            'warehouse',
            'warehouse_id',
            'product',
            'product_id',
            'supplier',
            'supplier_id',
            'quantity',
            'price',
            'description',
            'images',
            'is_available',
            'tags'
        ]

    def create(self, validated_data):
        warehouse = None
        product = None
        supplier = None

        if validated_data.get('warehouse_id'):
            try:
                warehouse_id = validated_data.pop('warehouse_id')
                warehouse = Warehouse.objects.get(id=warehouse_id)
            except Warehouse.DoesNotExist:
                raise WarehouseNotFoundException

        if validated_data.get('product_id'):
            try:
                product_id = validated_data.pop('product_id')
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise ProductNotFoundException

        if validated_data.get('supplier_id'):
            try:
                supplier_id = validated_data.pop('supplier_id')
                supplier = Supplier.objects.get(id=supplier_id)
            except Supplier.DoesNotExist:
                raise SupplierNotFoundException

        inventory = Inventory(
            **validated_data,
            warehouse=warehouse,
            product=product,
            supplier=supplier
        )
        try:
            inventory.save()
            return inventory
        except IntegrityError:
            raise UniqueInventoryException

    def update(self, instance, validated_data):
        try:
            if validated_data.get('warehouse_id'):
                try:
                    warehouse_id = validated_data.pop('warehouse_id')
                    warehouse = Warehouse.objects.get(id=warehouse_id)
                    instance.warehouse = warehouse
                except Warehouse.DoesNotExist:
                    raise WarehouseNotFoundException

            if validated_data.get('product_id'):
                try:
                    product_id = validated_data.pop('product_id')
                    product = Product.objects.get(id=product_id)
                    instance.product = product
                except Product.DoesNotExist:
                    raise ProductNotFoundException

            if validated_data.get('supplier_id'):
                try:
                    supplier_id = validated_data.pop('supplier_id')
                    supplier = Supplier.objects.get(id=supplier_id)
                    instance.supplier = supplier
                except Supplier.DoesNotExist:
                    raise SupplierNotFoundException

            return super().update(instance, validated_data)
        except IntegrityError:
            raise UniqueInventoryException


class InventoryListView(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()


class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
