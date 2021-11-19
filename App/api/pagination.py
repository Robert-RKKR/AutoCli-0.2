# Rest Django Import:
from rest_framework.pagination import PageNumberPagination


# Pagination's classes:
class SmallResultsPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_size = 10


class MediumResultsPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 100


class BigResultsPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_size = 1000