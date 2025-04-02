import re

from src.api import external_api
from src.generators import filter_by_currency, transaction_descriptions
from src.search import operation_finder
from src.processing import filter_by_state, sort_by_date
from src.readers import CSV_file_read, XLSX_file_read
from src.utils import connect_to_json
from src.widget import mask_account_card


def main_fail() -> str:
    """
    Если что-то не так, выводит ошибку.
    """
    return "Попробуйте ещё раз.\n"


def file_format():
    """
    Определяет расширение файла, с которым будем работать.
    """
    print("Добрый день, вы попали в программу для работы с банковскими транзакциями.")
    file = input(
        """Выберите номер формата файла:
    1. .json
    2. .csv
    3. .xlsx или .xls\n"""
    )
    if file == "1":
        print("Для работы выбран файл с расширением .json.\n")
        return connect_to_json('data/operations.json'), "json"
    if file == "2":
        print("Для работы выбран файл с расширением .csv.\n")
        return CSV_file_read(), "csv"
    if file == "3":
        print("Для работы выбран excel файл.\n")
        return XLSX_file_read(), "excel"
    else:
        print(main_fail())
        file_format()
        return [], ""


def status_sort(data):
    """
    Сортировка по статусу операции.
    """
    print("Выберите статус, по которому произойдет фильтрация.")
    status = input("Статусы: EXECUTED, CANCELED, PENDING\n")

    if status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        print("Недопустимый статус. Пожалуйста, выберите из предложенных вариантов.")
        return status_sort(data)
    return filter_by_state(data, status)



def date_sort(data):
    """
    Сортировка по дате.
    """
    user_sort = input("Отсортировать операции по дате? Да/Нет \n")
    if user_sort.lower() == "да":
        how_to_sort = input("По возрастанию(1) или по убыванию(2)?\n")
        if how_to_sort.lower() == "1":
            return sort_by_date(data)
        elif how_to_sort.lower() == "2":
            return sort_by_date(data, "decreasing")
        else:
            print(main_fail())
            date_sort(data)
            return []
    elif user_sort.lower() == "нет":
        return data
    else:
        print(main_fail())
        date_sort(data)
        return []


def value(data, file_type):
    """
    Сортировка по валюте.
    """
    user_sort = input("Выводить только рублевые? Да/Нет \n")
    if user_sort.lower() == "да":
        sorted_data = []
        for i in filter_by_currency(data, "RUB"):
            sorted_data.append(i)
        return sorted_data
    elif user_sort.lower() == "нет":
        return data
    else:
        print(main_fail())
        value(data, file_type)
        return []


def word_sort(data):
    """
    Сортировка по ключевым словам введенными пользователем.
    """
    user_sort = input("Фильтровать по определенному слову? Да/Нет\n")
    if user_sort.lower() == "да":
        to_find = input("Введите требуемое описание\n")
        return operation_finder(data, to_find)
    elif user_sort.lower() == "нет":
        return data
    else:
        print(main_fail())
        word_sort(data)
        return []


def main():
    """
    Основная функция, запускающая все предыдущие и завершающая работу.
    """
    data, file_type = file_format()
    data = status_sort(data)
    data = date_sort(data)
    data = value(data, file_type)
    data = word_sort(data)

    print("Секунду...")
    if data and len(data) != 0:
        print(f"Всего операций: {len(data)}\n")
        for operation in data:
            print(
                operation["date"],
                next(transaction_descriptions(data)),
            )
            if re.search("Перевод", operation["description"]):
                print(mask_account_card(operation["from"]), " -> ", mask_account_card(operation["to"]))
            else:
                print(mask_account_card(operation["to"]))
            print(f"Сумма: {external_api(operation)}руб. \n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()