from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api_app.constants import QUESTION_TYPE_TEXT, QUESTION_TYPE_RADIO, QUESTION_TYPE_CHECKBOX
from api_app.dtos.user_answer import UserAnswerDTO
from api_app.models import PollModel, QuestionModel
from api_app.serialisers.base import BaseSerializer


class AnswerSerializer(BaseSerializer):
    question_id = serializers.IntegerField()
    text_answer = serializers.CharField(required=False)
    answer_id = serializers.IntegerField(required=False)
    answer_ids = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate(self, attrs):
        question_id = attrs['question_id']
        text_answer = attrs.get('text_answer')
        answer_id = attrs.get('answer_id')
        answer_ids = attrs.get('answer_ids')

        poll_id = self.context['poll_id']
        poll = PollModel.objects.get(id=poll_id)

        if not poll.questions.filter(id=question_id).exists():
            raise ValidationError(f'Question with id {question_id} not found in poll {poll_id}.')

        question = QuestionModel.objects.get(id=question_id)

        if question.type == QUESTION_TYPE_TEXT:
            if not text_answer:
                raise ValidationError('text_answer is required for text questions.')
        elif question.type == QUESTION_TYPE_RADIO:
            if not answer_id:
                raise ValidationError('answer_id is required for radio questions.')
        elif question.type == QUESTION_TYPE_CHECKBOX:
            if not answer_ids:
                raise ValidationError('answer_ids is required for checkbox questions.')

        return attrs


class PassPollSerializer(BaseSerializer):
    poll_id = serializers.IntegerField()
    answers = AnswerSerializer(many=True)

    def validate(self, attrs):
        poll_id = attrs['poll_id']
        if not PollModel.objects.filter(id=poll_id).exists():
            raise ValidationError(f'Poll with id {poll_id} not found.')
        return attrs

    def get_dto(self):

        user = self.context['request'].user
        data = self.validated_data

        poll_id = data['poll_id']
        answers = data['answers']

        return [UserAnswerDTO(
            user_id=user.id if isinstance(user, User) else None,
            poll_id=poll_id,
            question_id=answer['question_id'],
            answer_ids=[answer.get('answer_id')] if answer.get('answer_id') else answer.get('answer_ids'),
            text_answer=answer.get('text_answer'),
        ) for answer in answers]
