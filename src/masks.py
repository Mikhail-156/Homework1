import logging
import os
from typing import Union

if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """
    Функция принимает на вход номер карты и возвращает его маску
    в формате XXXX XX** **** XXXX, где X - это цифры
    """
    logger.debug(f"Получение маски для номера карты: {card_number}")

    if len(str(card_number)) == 0:
        logger.error("Ошибка: Введите номер карты.")
        return "Введите номер карты"
    elif len(str(card_number)) != 16:
        logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
        return "Номер должин состоять из 16 цифр"
    elif str(card_number).isdigit():
        logger.info(f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}")
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    return "Номер должин содержать только цифры"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску в формате **XXXX,
    где X - это цифры
    """
    logger.debug(f"Получение маски для номера счета: {account_number}")

    if len(str(account_number)) == 0:
        logger.error("Ошибка: Введите номер Счета.")
        return "Введите номер Счета"
    elif len(str(account_number)) != 20:
        logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
        return "Номер должин состоять из 20 цифр"
    elif str(account_number).isdigit():
        logger.info(f"**{str(account_number)[-4:]}")
        return f"**{str(account_number)[-4:]}"
    return "Номер должин содержать только цифры"
