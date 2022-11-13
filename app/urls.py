from django.urls import path
from . import views

urlpatterns = [
    path('page<int:page>', views.index, name='questions'),

    path('hot', views.popular_questions, name='popular_questions'),
    path('hot/page<int:page>', views.popular_questions, name='popular_questions'),

    path('tag/<str:tag>', views.questions_by_tag, name='questions_by_tag'),
    path('tag/<str:tag>/page<int:page>', views.questions_by_tag, name='questions_by_tag'),

    path('tag/<str:tag>/popular', views.questions_tag_popular, name='questions_tag_popular'),
    path('tag/<str:tag>/popular/page<int:page>', views.questions_tag_popular, name='questions_tag_popular'),


    path('question/<int:id>', views.answers, name='answers'),
    path('question/<int:id>/page<int:page>', views.answers, name='answers'),

    path('login', views.login, name='login'),
    path('signup', views.signup, name='sign_up'),
    path('ask', views.ask, name='ask_question'),
    path('profile', views.profile, name='profile')
]
