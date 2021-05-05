from django.db import models

from api_app.constants import QUESTION_TYPE_CHOICES
from api_app.models.answer import AnswerModel
from api_app.models.base import BaseModel


class QuestionModel(BaseModel):
    text = models.CharField(max_length=1000)
    type = models.CharField(max_length=10, choices=QUESTION_TYPE_CHOICES)
    answers = models.ManyToManyField(
        AnswerModel,
        blank=True,
        help_text='Только для вопросов с выбором варианта!'
    )

    class Meta:
        verbose_name = 'Question'

    def __str__(self):
        return f'{self.type}: {self.text}'
