import requests
import os
from dotenv import load_dotenv
load_dotenv()



transaction = {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }


def external_api(transaction):
    code = transaction.get('operationAmount').get('currency',).get('code')
    amount = transaction.get('operationAmount').get('amount')

    if code == 'RUB':
        return float(amount)

    if code in ['EUR', 'USD']:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

            headers = {
                "apikey": os.getenv("API_KEY")
            }

            response = requests.request("GET", url, headers=headers)

            if response.status_code == 200:
                result = response.json()
                converted_amount = result.get('result')
                print(f"Конвертация: {converted_amount} рублей")
                return converted_amount
            else:
                print(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"An error occurred: {e.__class__.__name__} - {str(e)}")

external_api(transaction)