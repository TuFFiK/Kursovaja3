import json
from datetime import datetime


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


def mask_card_number(card_number):
    """
    Маскирует номер карты, отображая первые 6 цифр и последние 4.

    Parameters:
    - card_number (str): Номер карты.

    Returns:
    - str: Маскированный номер карты.
    """
    first_digit_index = next((i for i, char in enumerate(card_number) if char.isdigit()), None)

    if first_digit_index is not None:
        card_name = card_number[:first_digit_index].strip()
        digits_only = ''.join(char for char in card_number[first_digit_index:] if char.isdigit())

        masked_digits = ''.join([
            char if i < 6 or len(digits_only) - i <= 4 else '*'
            for i, char in enumerate(digits_only)
        ])

        blocks = [masked_digits[i:i + 4] for i in range(0, len(masked_digits), 4)]

        return f"{card_name} {' '.join(blocks)}"
    else:
        digits_only = ''.join(char for char in card_number if char.isdigit())
        masked_digits = ''.join([
            char if len(digits_only) - i <= 4 else '*'
            for i, char in enumerate(digits_only)
        ])

        blocks = [masked_digits[i:i + 4] for i in range(0, len(masked_digits), 4)]

        return ' '.join(blocks)


def mask_account_number(account_number):
    """
    Маскирует номер счета, отображая только последние 4 цифры.

    Parameters:
    - account_number (str): Номер счета.

    Returns:
    - str: Маскированный номер счета.
    """
    return '**' + account_number[-4:]


def format_transaction(transaction_data):
    """
    Форматирует данные о банковской операции для вывода на экран.

    Parameters:
    - transaction_data (dict): Данные о банковской операции.

    Returns:
    - str: Отформатированная строка для вывода.
    """
    date_str = transaction_data.get('date', '')
    date_obj = datetime.fromisoformat(date_str)
    formatted_date = date_obj.strftime('%d.%m.%Y')

    description = transaction_data.get('description', '')
    from_account = transaction_data.get('from', '')
    to_account = transaction_data.get('to', '')
    amount = transaction_data.get('operationAmount', {}).get('amount', '')
    currency = transaction_data.get('operationAmount', {}).get('currency', '')

    is_from_account = 'счет' in from_account.lower()
    is_to_account = 'счет' in to_account.lower()

    masked_from_account = 'Счет ' + mask_account_number(from_account) if is_from_account else mask_card_number(
        from_account)
    masked_to_account = 'Счет ' + mask_account_number(to_account) if is_to_account else mask_card_number(to_account)

    formatted_output = (
        f"{formatted_date} {description}\n"
        f"{masked_from_account} -> {masked_to_account}\n"
        f"{amount} {currency['name']}\n"
    )
    return formatted_output


def display_last_5_executed_transactions(file_path):
    """
    Выводит на экран последние 5 выполненных операций.

    Parameters:
    - file_path (str): Путь к файлу JSON с данными операций.
    """
    operations = load_operations(file_path)
    executed_transactions = [transaction for transaction in operations if transaction.get('state') == 'EXECUTED']
    last_5_executed = sorted(executed_transactions, key=lambda x: x.get('date'), reverse=True)[:5]

    for transaction in last_5_executed:
        formatted_transaction = format_transaction(transaction)
        print(formatted_transaction)
        print()


if __name__ == "__main__":
    file_path = '../operations.json'
    display_last_5_executed_transactions(file_path)
