import os
import pytest
from unittest.mock import patch
from src.api import external_api

transaction_usd = {
    "operationAmount": {
        "amount": "87941.37",
        "currency": {
            "code": "USD"
        }
    }
}

def test_api_key_exists():
    api_key = os.getenv("API_KEY")
    assert api_key is not None, "API_KEY Нету"