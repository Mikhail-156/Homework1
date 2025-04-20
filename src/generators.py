from typing import Dict, Iterator


def filter_by_currency(transactions: list[Dict], currency: str) -> Iterator[Dict]:
    """Генератор, который фильтрует транзакции по заданной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[Dict]) -> Iterator:
    """Генератор, который возвращает описание каждой транзакции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генератор номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    for number in range(start, stop + 1):
        number_card = f"{number:016d}"
        formatted_card_number = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:16]}"
        yield formatted_card_number
