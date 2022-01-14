from rest_framework.exceptions import APIException
from rest_framework import status


class ProductNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Product not found'
    default_code = 'product_not_found'
