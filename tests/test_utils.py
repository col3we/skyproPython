import pytest
import json
from unittest.mock import patch, mock_open
from src.utils import connect_to_json

@pytest.fixture
def mock_open_function():
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')) as mock_file:
        yield mock_file

def test_connect_to_json_success(mock_open_function):

    result = connect_to_json('dummy_path.json')
    assert result == {"key": "value"}
    mock_open_function.assert_called_once_with('dummy_path.json', 'r', encoding='utf-8')