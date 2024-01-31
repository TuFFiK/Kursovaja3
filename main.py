import json


def load_operations(file_path):
    """
        Загружает данные о банковских операциях из файла JSON.

        Parameters:
        - file_path (str): Путь к файлу JSON.

        Returns:
        - list: Список операций.
        """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def main():
    """
        Основная функция для демонстрации чтения данных о банковских операциях и вывода их в консоль.
        """
    file_path = 'operations.json'  # Предполагая, что вы извлекли файл из operations.zip
    operations = load_operations(file_path)
    print(json.dumps(operations, indent=2))


if __name__ == "__main__":
    main()
