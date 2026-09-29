from typing import Optional
from pydantic import BaseModel

class AnswerRequest(BaseModel):
    session_id: str
    answer: Optional[str] = None
    skip: Optional[bool] = False