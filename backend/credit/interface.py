from mypy_extensions import TypedDict
from datetime import datetime

class CreditInterface(TypedDict):
    id: int
    amount: float
    request_credit_id: int
    answer_date: datetime
    state: int
    user_id: int
    description: str

class RequestCreditInterface(TypedDict):
    id: int
    amount: float
    state: int
    user_id: int
