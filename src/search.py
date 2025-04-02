import re
from skyproPython.src.readers import CSV_file_read, XLSX_file_read


def operation_finder(data, user_request):
    return [op for op in data if "description" in op and re.search(user_request, str(op["description"]))]


def count_operation(data, categories):
    counts = {}
    for op in data:
        if "description" in op:
            for cat, words in categories.items():
                if any(word.lower() in str(op["description"]).lower() for word in words):
                    counts[cat] = counts.get(cat, 0) + 1
    return counts


def main():
    csv_data = CSV_file_read()

    excel_data = XLSX_file_read()

    all_data = csv_data + excel_data

    user_request = "Перевод"
    found_ops = operation_finder(all_data, user_request)
    print("Найденные операции:")
    print(found_ops)

    categories = {
        "Перевод между картами": ["Перевод с карты на карту"],
        "Перевод организации": ["Перевод организации"],
        "Открытие вклада": ["Открытие вклада"],
        "Перевод между счетами": ["Перевод со счета на счет"]
    }

    op_counts = count_operation(all_data, categories)
    print("\nКоличество операций по категориям:")
    print(op_counts)


if __name__ == "__main__":
    main()