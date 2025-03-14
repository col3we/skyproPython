import logging
import os
logger = logging.getLogger(__name__)
log_dir = '../logs'


file_handler = logging.FileHandler(os.path.join(log_dir, 'masks.log'))
file_formater = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

# Логирование сообщений
logger.debug('Debug')
logger.info('Info')


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, показывая первые 6 и последние 4 цифры,
    а остальные заменяет на символы '*'.
    """
    logger.debug('Замаскировано 6 цифр')
    return f"{card_number[:6]} {'*' * 6} {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, отображая только последние 4 цифры,
    предшествующие которым ставятся два символа '*'.
    """
    logger.info('Замаскировано последние 4 цифры')
    return f"**{account_number[-4:]}"

