import pytest
from src.decorators import log


@log()
def add(a, b):
    """
    Простая функция сложения двух чисел.
    """
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    """
    Тест функции сложения на корректных данных.
    Проверяет, что функция add возвращает правильные результаты для различных комбинаций чисел.
    """
    assert add(a, b) == expected


def test_add_non_numeric():
    """
    Тест функции сложения на некорректных данных.
    Проверяет, что функция add вызывает TypeError при попытке сложить нечисловые значения.
    """
    with pytest.raises(TypeError):
        add("a", 2)


def test_add_large_numbers():
    """
    Тест функции сложения на больших числах.
    Проверяет, что функция add правильно обрабатывает большие целые числа.
    """
    assert add(1000000, 2000000) == 3000000


def test_add_negative_numbers():
    """
    Тест функции сложения на отрицательных числах.
    Проверяет, что функция add правильно обрабатывает отрицательные целые числа.
    """
    assert add(-1, -2) == -3


def test_log_to_file_error(tmp_path):
    """
    Тест логирования в файл при возникновении ошибки.
    Проверяет, что декоратор log записывает информацию об ошибках в указанный файл.
    """
    filename = tmp_path / "log.txt"

    @log(filename=str(filename))
    def add(a, b):
        """
        Вспомогательная функция для тестирования логирования.
        """
        return a / b

    with pytest.raises(ZeroDivisionError):
        add(10, 0)

    with open(filename, 'r') as f:
        log_content = f.read()
        assert "Function 'add' started with args: (10, 0), kwargs: {}" in log_content
        assert "Function 'add' raised an exception: ZeroDivisionError with args: (10, 0), kwargs: {}" in log_content