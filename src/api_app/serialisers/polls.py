from rest_framework import serializers

from api_app.constants import QUESTION_TYPE_CHOICES
from api_app.serialisers.base import BaseSerializer


class AnswersSerializer(BaseSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    value = serializers.CharField()


class QuestionSerializer(BaseSerializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    type = serializers.ChoiceField(choices=QUESTION_TYPE_CHOICES)
    answers = AnswersSerializer(many=True)


class PollSerializer(BaseSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField()
    questions = QuestionSerializer(many=True)
