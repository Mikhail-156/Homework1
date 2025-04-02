from typing import Dict, Iterator


def filter_by_currency(transactions: list[Dict], currency: str) -> Iterator[Dict]:
    """Функция возврат итератор по транзакциям, у которых валюта совпадает с переданной"""
    for tx in transactions:
        if tx.get("currency") == currency:
            yield tx


def transaction_descriptions(transactions: list[Dict]) -> Iterator:
    """Функция возврата описание каждой транзакциями"""
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(x: int, y: int) -> Iterator:
    """Генератор номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    if x > y:
        raise ValueError("значение y должно быть меньше или равно значению x")
    for number in range(x, y + 1):
        number_card = str(number).zfill(16)
        formatted_card_number = (number_card[0:4]+" "+number_card[4:8]+" "+number_card[8:12]+" "+number_card[12:16])
        yield formatted_card_number
