import pytest

from src.widget import get_date, mask_account_card


def convert_date_test_() -> None:
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.fixture
def test() -> str:
    return "Счет **4305"


def test_with_fixture(test: str) -> None:
    assert test == mask_account_card("Счет 73654108430135874305")