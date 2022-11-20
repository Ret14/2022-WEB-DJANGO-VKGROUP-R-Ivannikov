from django.core.management import BaseCommand

from app.models import Profile, Tag, Question, Answer, QuestionLike, AnswerLike


class Command(BaseCommand):
    def handle(self, *args, **options):
        Profile.objects.all().delete()
        Tag.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()
        QuestionLike.objects.all().delete()
        AnswerLike.objects.all().delete()
