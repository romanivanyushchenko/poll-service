from django.contrib.auth.models import User
from django.db import models

from api_app.models import PollModel, QuestionModel, AnswerModel
from api_app.models.base import BaseModel


class UserAnswerModel(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(PollModel, on_delete=models.CASCADE, null=False)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, null=False)
    answers = models.ManyToManyField(AnswerModel)
    text_answer = models.CharField(max_length=1000, null=True)
