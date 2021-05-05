from django.db import models

from api_app.models.base import BaseModel


class AnswerModel(BaseModel):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Answer'

    def __str__(self):
        return f'{self.name}: {self.value}'
