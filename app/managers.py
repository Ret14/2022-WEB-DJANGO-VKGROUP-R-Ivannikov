from django.db import models
from django.db.models import Case, When, Sum, Count
from . import models as app_models


class QuestionManager(models.Manager):
    def get_new_questions(self):
        questions = self.annotate_rating()
        return questions.order_by('-asked_date')

    def get_popular_questions(self):
        questions = self.annotate_rating()
        return questions.order_by('-rating')

    def get_question_by_id(self, id):
        try:
            question = self.filter(id=id)
        except self.DoesNotExist:
            question = None

        return self.annotate_rating(question)[0]

    def get_questions_by_tag(self, tag):
        questions = app_models.Tag.objects.get(tag=tag).question_set.all()
        return self.annotate_rating(questions)

    def get_new_questions_by_tag(self, tag):
        return self.get_questions_by_tag(tag).order_by('-asked_date')

    def get_popular_questions_by_tag(self, tag):
        return self.get_questions_by_tag(tag).order_by('-rating')

    def annotate_rating(self, object=None):
        if object is None:
            return self.annotate(rating=Sum(Case(When(questionlike__is_upvote=True, then=1),
                                             When(questionlike__is_upvote=False, then=-1))))
        else:
            return object.annotate(rating=Sum(Case(When(questionlike__is_upvote=True, then=1),
                                                 When(questionlike__is_upvote=False, then=-1))))


class AnswerManager(models.Manager):
    def get_answers_by_question_id(self, id):
        answers = self.filter(question_id=id)
        return self.annotate_rating(answers)

    def annotate_rating(self, object=None):
        if object is None:
            return self.annotate(rating=Sum(Case(When(answerlike__is_upvote=True, then=1),
                                             When(answerlike__is_upvote=False, then=-1))))
        else:
            return object.annotate(rating=Sum(Case(When(answerlike__is_upvote=True, then=1),
                                                 When(answerlike__is_upvote=False, then=-1))))


class TagManager(models.Manager):
    def get_popular_tags(self, amount=20):
        return self.annotate(popularity=Count('question')).order_by('-popularity')[:amount]


class ProfileManager(models.Manager):
    def get_popular_users(self, amount=20):
        return self.annotate(popularity=Count('question') + Count('answer')).order_by('-popularity')[:amount]
