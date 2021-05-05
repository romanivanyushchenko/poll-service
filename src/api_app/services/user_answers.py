from typing import List

from django.db.transaction import atomic

from api_app.dtos.user_answer import UserAnswerDTO
from api_app.models import UserAnswerModel


@atomic
def create_user_answer(dto: UserAnswerDTO) -> UserAnswerModel:
    user_answer = UserAnswerModel.objects.create(
        user_id=dto.user_id,
        poll_id=dto.poll_id,
        question_id=dto.question_id,
        text_answer=dto.text_answer,
    )

    if dto.answer_ids:
        user_answer.answers.add(*dto.answer_ids)

    return user_answer


@atomic
def create_user_answers(dtos: List[UserAnswerDTO]) -> List[UserAnswerModel]:
    result = []
    for dto in dtos:
        user_answer = create_user_answer(dto)
        result.append(user_answer)
    return result
