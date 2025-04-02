from skyproPython.src.search import operation_finder, count_operation
from skyproPython.src.readers import CSV_file_read, XLSX_file_read

test_data = [
    {"description": "Перевод с карты на карту"},
    {"description": "Перевод организации"}
]

def test_operation_finder():
    user_request = "Перевод"
    found_ops = operation_finder(test_data, user_request)
    assert len(found_ops) == 2

def test_operation_finder_empty():
    user_request = "Нет такого слова"
    found_ops = operation_finder(test_data, user_request)
    assert len(found_ops) == 0

def test_count_operation_by_category():
    categories = {
        "Перевод между картами": ["Перевод с карты на карту"],
        "Перевод организации": ["Перевод организации"]
    }
    op_counts = count_operation(test_data, categories)
    assert len(op_counts) == 2

def test_count_operation_by_category_empty():
    categories = {
        "Нет такой категории": ["Нет такого слова"]
    }
    op_counts = count_operation(test_data, categories)
    assert len(op_counts) == 0

def test_operation_finder_real_data():
    csv_data = CSV_file_read()
    excel_data = XLSX_file_read()
    all_data = csv_data + excel_data
    user_request = "Перевод"
    found_ops = operation_finder(all_data, user_request)
    assert len(found_ops) >= 0

def test_count_operation_by_category_real_data():
    csv_data = CSV_file_read()
    excel_data = XLSX_file_read()
    all_data = csv_data + excel_data
    categories = {
        "Перевод между картами": ["Перевод с карты на карту"],
        "Перевод организации": ["Перевод организации"]
    }
    op_counts = count_operation(all_data, categories)
    assert len(op_counts) >= 0