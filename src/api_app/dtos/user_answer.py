from dataclasses import dataclass
from typing import Optional, List


@dataclass
class UserAnswerDTO:
    user_id: Optional[int]
    poll_id: int
    question_id: int
    answer_ids: Optional[List[int]]
    text_answer: Optional[str]
