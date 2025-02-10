from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date


def main() -> None:
    card_number = "7000792289606361"
    masked_card_number = get_mask_card_number(card_number)
    print(f"Маскированный номер карты: {masked_card_number}")

    account_number = "73654108430135874305"
    masked_account_number = get_mask_account(account_number)
    print(f"Маскированный номер счета: {masked_account_number}")

    cards = [
        "Visa Platinum 7000792289606361",
        "Maestro 7000792289606361",
        "Счет 73654108430135874305"
    ]

    for card in cards:
        masked = mask_account_card(card)
        print(masked)

    date_str = "2024-03-11T02:26:18.671407"
    formatted_date = get_date(date_str)
    print(formatted_date)


data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

print("Testing filter_by_state function with default state ('EXECUTED'):")
filtered_data_default = filter_by_state(data)
print("Filtered Data (state='EXECUTED'):", filtered_data_default)

print("\nTesting filter_by_state function with state 'CANCELED':")
filtered_data_canceled = filter_by_state(data, state='CANCELED')
print("Filtered Data (state='CANCELED'):", filtered_data_canceled)

print("\nTesting sort_by_date function (descending):")
sorted_data_descending = sort_by_date(data)
print("Sorted Data (descending):", sorted_data_descending)

sorted_data_ascending = sort_by_date(data, descending=False)
print("\nSorted Data (ascending):", sorted_data_ascending)

if __name__ == "__main__":
    main()