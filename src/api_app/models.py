from django.db import models

from api_app.constants import QUESTION_TYPE_CHOICES


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AnswerModel(BaseModel):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Answer'

    def __str__(self):
        return f'{self.name}: {self.value}'


class QuestionModel(BaseModel):
    text = models.CharField(max_length=1000)
    type = models.CharField(max_length=10, choices=QUESTION_TYPE_CHOICES)
    answers = models.ManyToManyField(
        AnswerModel,
        null=True,
        blank=True,
        help_text='Только для вопросов с выбором варианта!'
    )

    class Meta:
        verbose_name = 'Question'

    def __str__(self):
        return f'{self.type}: {self.text}'


class PollModel(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    description = models.CharField(max_length=1000, null=False, blank=True)
    questions = models.ManyToManyField(QuestionModel)

    class Meta:
        verbose_name = 'Poll'

    def __str__(self):
        return f'{self.name}: {self.description}'
