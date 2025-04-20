import json
import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')
logger = logging.getLogger("mylog")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/mylog.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path) -> list:
    """Загрузить транзакции из JSON-файла."""
    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Транзакции успешно загружены из файла: {file_path}")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком.")
                return []
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка при декодировании JSON из файла {file_path}: {e}")
            return []
