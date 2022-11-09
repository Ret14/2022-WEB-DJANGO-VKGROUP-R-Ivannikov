from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import Http404


def paginated_render(
        request, template_name, context, objects_list, per_page=20, page_number=1, **kwargs
):

    paginator = Paginator(objects_list, per_page)
    if page_number not in paginator.page_range:
        context['page_obj'] = paginator.get_page(1)
        return redirect(context['url_name'], **kwargs)

    context['page_obj'] = paginator.get_page(page_number)

    return render(request, template_name, context=context)


def get_question(questions_list, question_id):
    for question in questions_list:
        if question['id'] == question_id:
            return question

    raise Http404("Given query not found....")
