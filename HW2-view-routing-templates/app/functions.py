from django.core.paginator import Paginator
from django.http import Http404


def pagination(objects_list, per_page, page_number):
    paginator = Paginator(objects_list, per_page)
    if page_number not in paginator.page_range:
        return paginator.get_page(1)

    return paginator.get_page(page_number)


def get_question(questions_list, question_id):
    for question in questions_list:
        if question['id'] == question_id:
            return question

    raise Http404("Given query not found....")
