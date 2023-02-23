from src.average import find_average
import pytest


def test_average_function_with_correct_result():
    "Testa se a média de [4, 20] é 12"
    assert find_average([4, 20]) == 12


def test_average_function_with_wrong_result():
    "Testa se a média de [40, 2, 5, 5] é diferente de 12"
    assert find_average([40, 2, 5, 5]) != 12


def test_expression_should_be_at_least_one_array():
    with pytest.raises(ZeroDivisionError):
        find_average("")


def test_expression_should_with_numbers_only():
    with pytest.raises(TypeError):
        find_average(["a", "b", "c"])
