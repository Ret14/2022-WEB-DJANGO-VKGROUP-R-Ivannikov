from django.shortcuts import render
from . import models, functions

CONTEXT = {
    'tags': models.POPULAR_TAGS,
    'popular_users': models.POPULAR_USERS
}


def index(request, page=1):
    context = CONTEXT
    context['url_name'] = 'questions'
    return functions.paginated_render(
        request, 'new_questions.html', context, models.QUESTIONS, 20, page
    )


def questions_by_tag(request, tag='', page=1):
    context = CONTEXT
    context['url_name'] = 'questions_by_tag'
    context['tag'] = tag
    return functions.paginated_render(
        request, 'questions_by_tag.html', context, models.QUESTIONS, 20, page, tag=tag
    )


def questions_tag_popular(request, tag='', page=1):
    context = CONTEXT
    context['url_name'] = 'questions_tag_popular'
    context['tag'] = tag
    return functions.paginated_render(
        request, 'questions_tag_popular.html', context, models.QUESTIONS, 20, page, tag=tag
    )


def answers(request, id, page=1):
    context = CONTEXT
    context['url_name'] = 'answers'
    context['question_id'] = id
    context['question'] = functions.get_question(models.QUESTIONS, id)
    return functions.paginated_render(
        request, 'answers.html', context, context['question']['answers'], 20, page, id=id
    )


def popular_questions(request, page=1):
    context = CONTEXT
    context['url_name'] = 'popular_questions'
    return functions.paginated_render(
        request, 'hot_questions.html', context, models.QUESTIONS, 20, page
    )


def login(request):
    return render(request, template_name='login.html', context=CONTEXT)


def signup(request):
    return render(request, template_name='signup.html', context=CONTEXT)


def ask(request):
    return render(request, template_name='ask.html', context=CONTEXT)


def profile(request):
    return render(request, template_name='profile.html', context=CONTEXT)
