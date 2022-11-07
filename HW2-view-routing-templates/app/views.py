from django.shortcuts import render
from . import models
from . import functions

CONTEXT = {
    'tags': models.POPULAR_TAGS,
    'popular_users': models.POPULAR_USERS
}


def index(request, page=1):
    context = CONTEXT
    context['url_name'] = 'questions'
    context['page_obj'] = functions.pagination(models.QUESTIONS, 20, page)

    return render(request, template_name='new_questions.html', context=context)


def questions_by_tag(request, tag='', page=1):
    context = CONTEXT
    context['url_name'] = 'questions_by_tag'
    context['tag'] = tag
    context['page_obj'] = functions.pagination(models.QUESTIONS, 20, page)

    return render(request, template_name='questions_by_tag.html', context=context)


def hot(request, page=1):
    context = CONTEXT
    context['url_name'] = 'hot_questions'
    context['page_obj'] = functions.pagination(models.QUESTIONS, 20, page)
    return render(request, template_name='hot_questions.html', context=context)


def login(request):
    return render(request, template_name='login.html', context=CONTEXT)


def signup(request):
    return render(request, template_name='signup.html', context=CONTEXT)


def ask(request):
    return render(request, template_name='ask.html', context=CONTEXT)


def profile(request):
    return render(request, template_name='profile.html', context=CONTEXT)
