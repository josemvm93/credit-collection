from mypy_extensions import TypedDict


class IndicatorInterface(TypedDict):
    id: int
    name: str
    credit_id: int
    value: str