from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


def paginate(queryset, request):
    paginator = Pagination()

    paginated_queryset = paginator.paginate_queryset(queryset, request)

    page_info = {
        'count': paginator.page.paginator.count,
        'page_number': paginator.page.number,
        'next': paginator.get_next_link(),
        'previous': paginator.get_previous_link(),
    }

    return paginated_queryset, page_info
