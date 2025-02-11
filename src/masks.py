def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, показывая первые 6 и последние 4 цифры,
    а остальные заменяет на символы '*'.
    """
    return f"{card_number[:6]} {'*' * 6} {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, отображая только последние 4 цифры,
    предшествующие которым ставятся два символа '*'.
    """
    return f"**{account_number[-4:]}"
