import itertools
import random
import string
import traceback
from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import internet
from faker.providers import lorem

from app.models import Profile, Tag, Question, Answer, QuestionLike, AnswerLike


class Command(BaseCommand):
    help = 'Fill db with dummy data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', default=10000, type=int)

    def handle(self, *args, **options):
        ratio = options['ratio']
        fake = Faker()
        Faker.seed(0)
        fake.add_provider(internet)
        fake.add_provider(lorem)
        char_col = string.printable.replace(' ', '')
        try:
            Profile.objects.bulk_create(
                [
                    Profile(email=fake.email(),
                            username=fake.random_elements(elements=char_col, length=random.randint(8, 20)),
                            password=fake.password(length=random.randint(10, 50)))
                    for _ in range(ratio)
                ]
            )

            Tag.objects.bulk_create([
                Tag(tag=fake.random_elements(elements=char_col, length=random.randint(4, 15)))
                for _ in range(ratio)
            ])

            profiles = Profile.objects.all()
            tags = Tag.objects.all()

            Question.objects.bulk_create([
                Question(author_id=random.choice(profiles), title=fake.text(max_nb_chars=200),
                         text=fake.text(max_nb_chars=500))
                for _ in range(ratio * 10)
            ])
            question_ids = list(Question.objects.values_list('id', flat=True))
            tag_ids = list(Tag.objects.values_list('id', flat=True))

            for question_id in question_ids:
                question_to_tag_links = []
                question_tags = random.sample(tag_ids, random.randint(1,4))
                for tag in question_tags:
                    tag_question = Question.tags.through(question_id=question_id, tag_id=tag)
                    question_to_tag_links.append(tag_question)

                Question.tags.through.objects.bulk_create(question_to_tag_links)

            users = Profile.objects.all()
            questions = Question.objects.all()
            Answer.objects.bulk_create([
                Answer(author_id=random.choice(users), question_id=random.choice(questions),
                       text=fake.text(max_nb_chars=random.randint(200, 1000)))
                for _ in range(ratio * 100)
            ])
            question_user_list = random.sample(set(itertools.product(users, questions)), ratio * 100)
            QuestionLike.objects.bulk_create([
                QuestionLike(user_id=question_user_list[num][0], question_id=question_user_list[num][1],
                             is_upvote=bool(random.getrandbits(1)))
                for num in range(ratio * 100)
            ])

            answers = Answer.objects.all()

            answer_user_list = random.sample(set(itertools.product(users, answers)), ratio * 100)

            AnswerLike.objects.bulk_create([
                AnswerLike(user_id=answer_user_list[num][0], answer_id=answer_user_list[num][1],
                           is_upvote=bool(random.getrandbits(1)))
                for num in range(ratio * 100)
            ])

        except Exception:
            Profile.objects.all().delete()
            Tag.objects.all().delete()
            Question.objects.all().delete()
            Answer.objects.all().delete()
            QuestionLike.objects.all().delete()
            AnswerLike.objects.all().delete()
            traceback.print_exc()
