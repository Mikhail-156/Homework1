import re
from collections import Counter
from datetime import datetime
from typing import Any


def filter_by_state(bank_transaction: list[dict], state: str ) -> list[dict]:
    """Функция возврата словарей банковских операций по ключу"""
    return [op for op in bank_transaction if op.get("state", "") == state]


def sort_by_date(data_logs: list[dict], reverse: bool = True) -> list:
    """Функция сортировке банковских операций по дате"""
    return sorted(data_logs, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)


def search_by_string(operations_list: list[dict], search_string: str) -> list[dict]:
    """Функция поиск в списке операций по заданной строке."""
    operations_found = []
    pattern = rf"{search_string}"

    for operation in operations_list:
        descr = str(operation["description"])
        match = re.search(pattern, descr, flags=re.IGNORECASE)
        if match:
            operations_found.append(operation)

    return operations_found


def count_operations_by_categories(operations_list: list[dict], user_categories: list) -> dict:
    """Функция подсчета операций по заданным пользователем категориям."""
    counted = Counter()

    for operation in operations_list:
        descr = str(operation["description"]).lower()
        if len(descr) > 0:
            for category in user_categories:
                if len(category) > 0:
                    if category.lower() in descr:
                        counted[category] += 1
                else:
                    print("Ошибка запроса!")
                    return {}
        else:
            print("Ошибка запроса!")
            return {}

    return dict(counted)
