def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета, показывая только часть информации.
    """
    last_index = 0

    for i in range(len(account_info)):
        if account_info[i] == ' ':
            last_index = i

    card_type = account_info[:last_index]
    card_number = account_info[last_index + 1:]

    if 'Счет' in card_type:
        masked_number = f"{card_type} **{card_number[-4:]}"
    else:
        masked_number = f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_number


def get_date(date_str: str) -> str:
    """
    Преобразует строку даты в формат дд.мм.гггг.
    """
    year = date_str[0:4]
    month = date_str[5:7]
    day = date_str[8:10]

    return f"{day}.{month}.{year}"