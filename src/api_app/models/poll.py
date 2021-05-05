from django.db import models

from api_app.models.base import BaseModel
from api_app.models.question import QuestionModel


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
