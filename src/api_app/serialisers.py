from rest_framework import serializers

from api_app.constants import QUESTION_TYPE_CHOICES


class BaseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AnswersSerializer(BaseSerializer):
    name = serializers.CharField()
    value = serializers.CharField()


class QuestionSerializer(BaseSerializer):
    text = serializers.CharField()
    type = serializers.ChoiceField(choices=QUESTION_TYPE_CHOICES)
    answers = AnswersSerializer(many=True)


class PollSerializer(BaseSerializer):
    name = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField()
    questions = QuestionSerializer(many=True)
