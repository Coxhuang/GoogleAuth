from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination, CursorPagination
from rest_framework.response import Response
#自定义分页类
class MyPageNumberPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 3
    #默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    #最大页数不超过10
    max_page_size = 10
    #获取页码数的
    page_query_param = "page"
    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'pagination': self.page.paginator.count,
            'page_size': self.page.paginator.per_page,
            'page': self.page.start_index(),
            'success': False
        })