from django.shortcuts import render
from . import models, functions

CONTEXT = {
    'tags': models.Tag.objects.get_popular_tags(20),
    'popular_users': models.Profile.objects.get_popular_users(20)
}


def index(request, page=1):
    context = CONTEXT
    context['url_name'] = 'questions'
    new_questions = models.Question.objects.get_new_questions()
    context['page_obj'] = functions.pagination(new_questions, 20, page)

    return render(request, 'new_questions.html', context)


def questions_by_tag(request, tag='', page=1):
    context = CONTEXT
    context['url_name'] = 'questions_by_tag'
    context['tag'] = tag
    tagged_questions = models.Question.objects.get_new_questions_by_tag(tag)
    context['page_obj'] = functions.pagination(tagged_questions, 20, page)

    return render(request, 'questions_by_tag.html', context)


def questions_tag_popular(request, tag, page=1):
    context = CONTEXT
    context['url_name'] = 'questions_tag_popular'
    context['tag'] = tag
    tagged_questions = models.Question.objects.get_popular_questions_by_tag(tag)
    context['page_obj'] = functions.pagination(tagged_questions, 20, page)

    return render(request, 'questions_tag_popular.html', context)


def answers(request, id, page=1):
    context = CONTEXT
    context['url_name'] = 'answers'
    context['question'] = models.Question.objects.get_question_by_id(id)
    question_answers = models.Answer.objects.get_answers_by_question_id(id)
    context['page_obj'] = functions.pagination(question_answers, 20, page)

    return render(request, 'answers.html', context)


def popular_questions(request, page=1):
    context = CONTEXT
    context['url_name'] = 'popular_questions'
    pop_questions = models.Question.objects.get_popular_questions()
    context['page_obj'] = functions.pagination(pop_questions, 20, page)

    return render(request, 'hot_questions.html', context)


def login(request):
    return render(request, template_name='login.html', context=CONTEXT)


def signup(request):
    return render(request, template_name='signup.html', context=CONTEXT)


def ask(request):
    return render(request, template_name='ask.html', context=CONTEXT)


def profile(request):
    return render(request, template_name='profile.html', context=CONTEXT)
