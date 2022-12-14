from django.core.paginator import Paginator

def pagination(objects_list, per_page, page_number):
    paginator = Paginator(objects_list, per_page)
    if page_number not in paginator.page_range:
        return paginator.get_page(1)

    return paginator.get_page(page_number)
