from datetime import datetime

from src import masks


def mask_account_card(name_for_mask: str) -> str:
    """Функция маскировки для карт или счетов"""
    if name_for_mask == "":
        return ""

    parts = name_for_mask.split()
    card_type = " ".join(parts[:-1])
    card_number_str = parts[-1]

    if not card_number_str.isdigit():
        return "Неверный формат номера счета или карты"

    try:
        card_number = int(card_number_str)
        if "счет" in card_type.lower():
            masked_number = masks.get_mask_account(card_number)
        elif len(card_number_str) == 16:
            masked_number = masks.get_mask_card_number(card_number)
        else:
            raise ValueError("Неверный формат номера счета или карты")
        return f"{card_type} {masked_number}"
    except ValueError as e:
        return f"Ошибка: {e}"


def get_date(my_date: str) -> str:
    """Функция смены вормата даты и вреня"""
    try:
        date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "неверный формат"
