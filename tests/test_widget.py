import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "name_for_mask, expected_resilt",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 5185373029202738", "MasterCard 5185 37** **** 2738"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Invalid Card 1234", "Ошибка: Неверный формат номера счета или карты"),
        ("", ""),
        ("Счет 12345678901234567ghj", "Неверный формат номера счета или карты"),
        ("Visa Platinum 7000792289606ghy", "Неверный формат номера счета или карты"),
    ],
)
def test_mask_account_card(name_for_mask: str, expected_resilt: str) -> None:
    assert mask_account_card(name_for_mask) == expected_resilt


@pytest.mark.parametrize(
    "my_date, expected_resilt",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", "неверный формат"),
        ("2024-03-11", "неверный формат"),
    ],
)
def test_get_date(my_date: str, expected_resilt: str) -> None:
    assert get_date(my_date) == expected_resilt
