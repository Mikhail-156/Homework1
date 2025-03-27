from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_for_mask: str) -> str:
    """Функция маскировки для карт и счетов"""
    if len(name_for_mask) != 0:
        list_ = name_for_mask.split()
        if list_[-1].isalpha():
            return "Введите номер"
        elif len(list_[-1]) == 20:
            return f"{list_[0]} {get_mask_account(list_[1])}"
        elif list_[1].isalpha() and len(list_[-1]) == 16:
            return f"{list_[0]} {list_[1]} {get_mask_card_number(list_[-1])}"
        elif len(list_[-1]) == 16:
            return f"{list_[0]} {get_mask_card_number(list_[1])}"
    return "Введите данные"


def get_date(my_date: str) -> str:
    """Функция смены вормата даты и вреня"""
    try:
        date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "неверный формат"
