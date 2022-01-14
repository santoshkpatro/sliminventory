from rest_framework import generics, serializers, permissions
from app.models import Warehouse, User
from app.exceptions.user import UserNotFoundException


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'avatar']


class WarehouseSerializer(serializers.ModelSerializer):
    manager_id = serializers.IntegerField(write_only=True, required=False)
    manager = ManagerSerializer(read_only=True)

    class Meta:
        model = Warehouse
        fields = [
            'id',
            'uuid',
            'manager',
            'manager_id',
            'name',
            'capacity',
            'description',
            'location',
            'profile',
            'is_operational'
        ]

    def create(self, validated_data):
        manager = None
        if validated_data.get('manager_id'):
            manager_id = validated_data.pop('manager_id')
            try:
                manager = User.objects.get(id=manager_id)
            except User.DoesNotExist:
                raise UserNotFoundException
        warehouse = Warehouse(**validated_data, manager=manager)
        warehouse.save()

        return warehouse

    def update(self, instance, validated_data):
        if validated_data.get('manager_id'):
            manager_id = validated_data.pop('manager_id')
            try:
                manager = User.objects.get(id=manager_id)
                instance.manager = manager
            except User.DoesNotExist:
                raise UserNotFoundException
        return super().update(instance, validated_data)


class WarehouseListView(generics.ListCreateAPIView):
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class WarehouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()
    permission_classes = [permissions.IsAuthenticated]
