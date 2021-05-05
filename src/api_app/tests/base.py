from datetime import datetime

from model_bakery import baker

from api_app.constants import QUESTION_TYPE_TEXT, QUESTION_TYPE_RADIO, QUESTION_TYPE_CHECKBOX


def create_test_poll():
    questions = [
        baker.make(
            'api_app.QuestionModel',
            text='First question?',
            type=QUESTION_TYPE_TEXT,
        ),
        baker.make(
            'api_app.QuestionModel',
            text='Second question?',
            type=QUESTION_TYPE_RADIO,
            answers=[
                baker.make('api_app.AnswerModel', name='1', value='One of me 1.'),
                baker.make('api_app.AnswerModel', name='2', value='One of me 2.'),
                baker.make('api_app.AnswerModel', name='3', value='One of me 3.'),
            ]
        ),
        baker.make(
            'api_app.QuestionModel',
            text='Third question?',
            type=QUESTION_TYPE_CHECKBOX,
            answers=[
                baker.make('api_app.AnswerModel', name='1', value='Any of my 1.'),
                baker.make('api_app.AnswerModel', name='2', value='Any of my 2.'),
                baker.make('api_app.AnswerModel', name='3', value='Any of my 3.'),
            ]
        ),
    ]

    poll = baker.make(
        'api_app.PollModel',
        name='Test Poll',
        start_date=datetime.today(),
        end_date=datetime.today(),
        description='Super!',
        questions=questions
    )
    return poll
