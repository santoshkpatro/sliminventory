from rest_framework.exceptions import APIException
from rest_framework import status


class SupplierNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Supplier not found'
    default_code = 'supplier_not_found'
