from datetime import datetime


def filter_by_state(bank_transaction: list[dict], state: str = "EXECUTED") -> list:
    """Функция возврата словарей банковских операций по ключу"""
    return [op for op in bank_transaction if op.get("state") == state]


def sort_by_date(data_logs: list[dict], reverse: bool = True) -> list:
    """Функция сортировке банковских операций по дате"""
    return sorted(data_logs, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
