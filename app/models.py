from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Profile(AbstractUser):
    avatar = models.ImageField(upload_to='uploads', default='static/img/lancer.png')
    # rating = models.IntegerField()


class Tag(models.Model):
    tag = models.CharField(unique=True, max_length=100)

    @property
    def rating(self):
        return Question.objects.filter(tags__in=self).count()


class Question(models.Model):
    author_id = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=1000)
    text = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    datetime = models.DateTimeField(auto_now=True)
    # rating = models.IntegerField()

    @property
    def rating(self):
        return QuestionLike.objects.filter(question_id=self, is_upvote=True).count() - \
               QuestionLike.objects.filter(question_id=self, is_upvote=False).count()


class Answer(models.Model):
    author_id = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1000)
    # rating = models.IntegerField()

    @property
    def rating(self):
        return AnswerLike.objects.filter(answer_id=self, is_upvote=True).count() - \
               AnswerLike.objects.filter(answer_id=self, is_upvote=False).count()


class QuestionLike(models.Model):
    user_id = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user_id', 'question_id'), name='unique_user_question')
        ]


class AnswerLike(models.Model):
    user_id = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user_id', 'answer_id'), name='unique_user_answer')
        ]



QUESTIONS = [
    {
        'id': question_id,
        'title': f'Title of question #{question_id}',
        'text': f'Text of question #{question_id}',
        'tags': ['python', 'django', 'javascript'],
        'rating': question_id,
        'asked_date': f'Jan {question_id}, 2018 at 17:17',
        'user': {
            'username': f'User{question_id}',
            'rating': question_id + 5,
            'avatar_path': 'img/chris.png'
        },
        'answers': [
            {
                'text': f'Text of answer #{answer_number}',
                'author': {
                    'username': f'User{answer_number}',
                    'rating': answer_number + 6,
                    'avatar_path': 'img/chris.png'
                },
                'date': f'Jan {answer_number}, 2018 at 17:17',
                'rating': answer_number
            } for answer_number in range(50)
        ]

    } for question_id in range(50)
]

POPULAR_TAGS = [
    {'name': 'python', 'count': 252478},
    {'name': 'kotlin', 'count': 288478},
    {'name': 'javascript', 'count': 252998},
    {'name': 'django', 'count': 258778},
    {'name': 'pascal', 'count': 284478},
    {'name': 'c++', 'count': 252471},
]

POPULAR_USERS = [
    'Jojo', 'Dio', 'Johnathan Joestar', 'Jojo', 'Dio', 'Johnathan Joestar'
]
