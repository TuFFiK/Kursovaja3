import json
import pytest
from src.bank_transfers import mask_card_number, mask_account_number, display_last_5_executed_transactions, \
    format_transaction

TEST_JSON_FILE_PATH = 'test_operations.json'

test_data = [
    {
        "state": "EXECUTED",
        "date": "2023-10-25T12:34:56.789Z",
        "description": "Test 1",
        "from": "Maestro 7810 8465 **** 5568",
        "to": "123456789",
        "operationAmount": {
            "amount": 100.0,
            "currency": {"name": "USD"}
        }
    },
    {
        "state": "EXECUTED",
        "date": "2023-10-24T12:34:56.789Z",
        "description": "Test 2",
        "from": "Maestro 7810 8465 **** 5568",
        "to": "987654321",
        "operationAmount": {
            "amount": 200.0,
            "currency": {"name": "EUR"}
        }
    },
    {
        "state": "EXECUTED",
        "date": "2023-10-23T12:34:56.789Z",
        "description": "Test 3",
        "from": "543210987",
        "to": "Maestro 7810 8465 **** 5568",
        "operationAmount": {
            "amount": 300.0,
            "currency": {"name": "GBP"}
        }
    }
]


def test_mask_card_number():
    card_number = "Maestro 7810 8465 **** 5568"
    masked_card = mask_card_number(card_number)
    print(f"Masked Card Number: {masked_card}")
    assert isinstance(masked_card, str)


def test_mask_account_number():
    account_number = "123456789"
    masked_account = mask_account_number(account_number)
    print(f"Masked Account Number: {masked_account}")
    assert isinstance(masked_account, str)


def test_format_transaction():
    transaction_data = {
        "date": "2023-10-25T12:34:56.789Z",
        "description": "Test Transaction",
        "from": "Maestro 7810 8465 **** 5568",
        "to": "123456789",
        "operationAmount": {"amount": 100.0, "currency": {"name": "USD"}},
    }
    formatted_transaction = format_transaction(transaction_data)
    print(f"Formatted Transaction: {formatted_transaction}")
    assert isinstance(formatted_transaction, str)


with open(TEST_JSON_FILE_PATH, 'w', encoding='utf-8') as test_file:
    json.dump(test_data, test_file)


def test_display_last_5_executed_transactions():
    display_last_5_executed_transactions(TEST_JSON_FILE_PATH)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
