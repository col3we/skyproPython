def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    Возвращает новый список словарей с указанным состоянием.
    """
    filtered_data = []
    for item in data:
        if item.get('state') == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате.
    Возвращает новый отсортированный список.
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
