import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected_resilt", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7676700079289606361", "Номер должин состоять из 16 цифр"),
    ("fdff792289606361", "Номер должин содержать только цифры"),
    ("", "Введите номер карты")
])
def test_get_mask_card_number(card_number: str, expected_resilt: str) -> None:
    assert get_mask_card_number(card_number) == expected_resilt


@pytest.mark.parametrize("account_number, expected_resilt", [
    ("73654108430135874305", "**4305"),
    ("654108430135874305", "Номер должин состоять из 20 цифр"),
    ("as654108430135874305", "Номер должин содержать только цифры"),
    ("", "Введите номер Счета")
])
def test_get_mask_account(account_number: str, expected_resilt: str) -> None:
    assert get_mask_account(account_number) == expected_resilt
