import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "name_for_mask, expected_resilt",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("", "Введите данные"),
        ("Maestro", "Введите номер"),
        ("Счет", "Введите номер"),
        ("Visa Platinum", "Введите номер"),
        ("Visa Classic gf31982476737658", "Visa Classic Номер должин содержать только цифры"),
        # ("", ""),
        ("Счет пп686473678894779589", "Счет Номер должин содержать только цифры"),
        ("Maestro dd96837868705199", "Maestro Номер должин содержать только цифры"),
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
