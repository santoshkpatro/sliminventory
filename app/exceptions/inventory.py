from rest_framework.exceptions import APIException
from rest_framework import status


class UniqueInventoryException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Inventory, Supplier, Product is not unique'
    default_code = 'unique_error'
