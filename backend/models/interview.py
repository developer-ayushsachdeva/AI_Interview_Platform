from enum import Enum
from typing import Optional

from pydantic import BaseModel


class InterviewEnumStatus(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELED = "canceled"


class Answer(BaseModel):
    question: str
    answer: Optional[str] = None
    skip: bool = False


class InterviewSession(BaseModel):
    session_id: str
    questions: list[str] = []
    status: InterviewEnumStatus = InterviewEnumStatus.SCHEDULED
    answers: list[Answer] = []
    current_index: int = 0
    introText: str = ""