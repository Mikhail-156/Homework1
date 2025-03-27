from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Функция которя скрывает номет катры"""
    if len(str(card_number)) == 0:
        return "Введите номер карты"
    elif len(str(card_number)) != 16:
        return "Номер должин состоять из 16 цифр"
    elif card_number.isdigit():
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    return "Номер должин содержать только цифры"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция которя скрывает номет счета"""
    if len(str(account_number)) == 0:
        return "Введите номер Счета"
    elif len(str(account_number)) != 20:
        return "Номер должин состоять из 20 цифр"
    elif account_number.isdigit():
        return f"**{str(account_number)[-4:]}"
    return "Номер должин содержать только цифры"
