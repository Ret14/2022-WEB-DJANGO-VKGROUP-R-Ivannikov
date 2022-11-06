from django.db import models

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
        }

    } for question_id in range(50)
]

POPULAR_TAGS = [
    {'name': 'python', 'count': 252478},
    {'name': 'kotlin', 'count': 288478},
    {'name': 'javascript', 'count': 252998},
    {'name': 'django', 'count': 258778},
    {'name': 'kotlin', 'count': 284478},
    {'name': 'python', 'count': 252471},
]

POPULAR_USERS = [
    'Jojo', 'Dio', 'Johnathan Joestar', 'Jojo', 'Dio', 'Johnathan Joestar'
]
