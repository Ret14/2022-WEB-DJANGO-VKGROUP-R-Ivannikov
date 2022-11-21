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
    fake = Faker()
    random_char_set = string.ascii_letters

    def add_arguments(self, parser):
        parser.add_argument('ratio', default=10000, type=int)

    def handle(self, *args, **options):
        ratio = options['ratio']
        Faker.seed(0)
        self.fake.add_provider(internet)
        self.fake.add_provider(lorem)
        try:
            self.create_tags(ratio)
            self.create_profiles(ratio)
            self.create_questions_with_tags(ratio * 10)
            self.create_answers(ratio * 100)
            self.create_question_and_answer_likes(ratio * 200)

        except Exception:
            Profile.objects.all().delete()
            Tag.objects.all().delete()
            Question.objects.all().delete()
            Answer.objects.all().delete()
            QuestionLike.objects.all().delete()
            AnswerLike.objects.all().delete()
            traceback.print_exc()

    def create_random_string(self, a, b):
        return ''.join(self.fake.random_elements(elements=self.random_char_set,
                                                 length=random.randint(a, b)))

    def create_tags(self, amount):
        tags = [Tag(tag=self.create_random_string(5, 20))
                for _ in range(amount)]

        Tag.objects.bulk_create(tags)

    def create_profiles(self, amount):
        profiles = [Profile(email=self.fake.email(), username=self.create_random_string(5, 20),
                            password=self.fake.password(length=random.randint(20, 50)),
                            avatar=f'/img/test-avatar-{random.randint(0, 2)}.png')
                    for _ in range(amount)]

        Profile.objects.bulk_create(profiles)

    def create_questions_with_tags(self, questions_amount):
        profile_ids = list(Profile.objects.values_list('id', flat=True))

        questions = [Question(author_id=random.choice(profile_ids),
                              title=self.fake.text(max_nb_chars=random.randint(100, 200)),
                              text=self.fake.text(max_nb_chars=random.randint(400, 1000)))
                     for _ in range(questions_amount)]

        Question.objects.bulk_create(questions)

        tag_ids = list(Tag.objects.values_list('id', flat=True))
        question_ids = list(Question.objects.values_list('id', flat=True))

        question_to_tag_links = []
        for question_id in question_ids:
            question_tags = random.sample(tag_ids, random.randint(1, 4))
            for tag_id in question_tags:
                tag_question = Question.tags.through(question_id=question_id, tag_id=tag_id)
                question_to_tag_links.append(tag_question)

        Question.tags.through.objects.bulk_create(question_to_tag_links)

    def create_answers(self, amount):
        author_ids = list(Profile.objects.values_list('id', flat=True))
        question_ids = list(Question.objects.values_list('id', flat=True))

        answers = [Answer(author_id=random.choice(author_ids), question_id=random.choice(question_ids),
                          text=self.fake.text(max_nb_chars=random.randint(100, 1000)))
                   for _ in range(amount)]

        Answer.objects.bulk_create(answers)

    def create_question_and_answer_likes(self, amount):
        user_ids = list(Profile.objects.values_list('id', flat=True))
        question_ids = list(Question.objects.values_list('id', flat=True))

        question_user_list = random.sample(set(itertools.product(user_ids, question_ids)), amount // 2)

        question_likes = [QuestionLike(user_id=question_user_list[num][0], question_id=question_user_list[num][1],
                                       is_upvote=bool(random.getrandbits(1)))
                          for num in range(amount // 2)]

        QuestionLike.objects.bulk_create(question_likes)

        answer_ids = list(Answer.objects.values_list('id', flat=True))
        answer_user_list = random.sample(set(itertools.product(user_ids, answer_ids)), amount // 2)

        answer_likes = [AnswerLike(user_id=answer_user_list[num][0], answer_id=answer_user_list[num][1],
                                   is_upvote=bool(random.getrandbits(1)))
                        for num in range(amount // 2)]

        AnswerLike.objects.bulk_create(answer_likes)
