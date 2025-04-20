import json
import os


def load_transactions(file_path):
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
