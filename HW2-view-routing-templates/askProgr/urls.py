"""askProgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='questions'),
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

