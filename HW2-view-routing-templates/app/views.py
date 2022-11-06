from django.shortcuts import render
from . import models
from django.core.paginator import Paginator


CONTEXT = {
    'tags': models.POPULAR_TAGS,
    'popular_users': models.POPULAR_USERS
}


def index(request, num=1):
    context = CONTEXT
    context['url_name'] = 'questions'
    paginator = Paginator(models.QUESTIONS, 20)
    # page_number = request.GET.get('page')
    context['page_obj'] = paginator.get_page(num)

    return render(request, template_name='new_questions.html', context=context)


def hot(request):
    context = CONTEXT
    context['questions'] = models.QUESTIONS
    return render(request, template_name='hot_questions.html', context=context)


def login(request):
    return render(request, template_name='login.html', context=CONTEXT)


def signup(request):
    return render(request, template_name='signup.html', context=CONTEXT)
