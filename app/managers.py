from django.db import models
from app.models import Tag


# class TagManager(models.Manager):
#
#     def get_popular_tags(self, amount=20):
#         return self.order_by('rating')[:amount]
#
#
# class ProfileManager(models.Manager):
#
#     def get_popular_users(self, amount=20):
#         return self.order_by('rating')[:amount]
#
#
# class QuestionManager(models.Manager):
#
#     def get_popular_questions(self):
#         return self.order_by('rating')
#
#     def get_new_questions(self):
#         return self.order_by('datetime')
#
#     def get_questions_by_tag(self, tag_name):
#         # tag_id = Tag.objects.filter(tag_name=tag_name)[0].values('id')['id']
#         return self.filter(tag=tag_name)
