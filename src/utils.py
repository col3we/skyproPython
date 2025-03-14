import json
from json import JSONDecodeError
import logging
import os

logger = logging.getLogger(__name__)
log_dir = '../logs'


logger.debug('Debug ')
logger.info('Info ')
logger.warning('Warning ')
logger.error('Error ')
logger.critical("Critical ")

file_handler = logging.FileHandler(os.path.join(log_dir, 'utils.log'))
file_formater = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)




def connect_to_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.debug(f'Successfully {path}')
            return data
    except FileNotFoundError as e:
        logger.error(f'File not found: {e}')
        print(f'File not found: {e}')
        return '[]'
    except JSONDecodeError as e:
        logger.error(f'JSON decode error: {e}')
        print(f'JSON decode error: {e}')
        return '[]'



if __name__ == "__main__":
    json_data = connect_to_json(r'C:\Users\Makarov.F\PycharmProjects\pythonProject\data\operations.json')
    print(json_data)