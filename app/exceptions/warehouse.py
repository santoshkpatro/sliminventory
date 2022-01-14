from rest_framework.exceptions import APIException
from rest_framework import status


class WarehouseNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Warehouse not found'
    default_code = 'warehouse_not_found'
