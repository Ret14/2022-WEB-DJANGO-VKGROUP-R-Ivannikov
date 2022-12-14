from django.db import models
from django.contrib.auth.models import AbstractUser
from app.managers import QuestionManager, AnswerManager, TagManager, ProfileManager


class Profile(AbstractUser):
    avatar = models.ImageField(upload_to='uploads', default='static/img/test-avatar-1.png')
    objects = ProfileManager()

    def get_rating(self):
        return Question.objects.filter(author_id=self.id).count() + Answer.objects.filter(author_id=self.id).count()
    def __str__(self):
        return self.username


class Tag(models.Model):
    tag = models.CharField(unique=True, max_length=20)
    objects = TagManager()

    def __str__(self):
        return self.tag


class Question(models.Model):
    author = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    asked_date = models.DateTimeField(auto_now=True)
    objects = QuestionManager()

    def get_rating(self):
        return QuestionLike.objects.filter(question_id=self.id, is_upvote=True).count() -\
               QuestionLike.objects.filter(question_id=self.id, is_upvote=False).count()


class Answer(models.Model):
    author = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1000)
    objects = AnswerManager()

    def get_rating(self):
        return AnswerLike.objects.filter(answer_id=self.id, is_upvote=True).count() -\
               AnswerLike.objects.filter(answer_id=self.id, is_upvote=False).count()



class QuestionLike(models.Model):
    user = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'question'), name='unique_user_question')
        ]


class AnswerLike(models.Model):
    user = models.ForeignKey(Profile, models.SET_NULL, blank=True, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'answer'), name='unique_user_answer')
        ]