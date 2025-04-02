def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по заданному коду валюты.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Функция transaction_descriptions возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield str(description)


def card_number_generator(first_numb: int, second_numb: int):
    """
    card_number_generator создает номера карт в указанном диапазоне.
    """
    for numb in range(first_numb, second_numb + 1):
        card = f"{numb:0>16}"
        new_card = f"{card[-16:-12]} {card[-12:-8]} {card[-8:-4]} {card[-4:]}"
        yield new_card