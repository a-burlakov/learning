from main import division
import pytest

# Параметризируемый тест.
@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5),
                                                   (44, 22, 2)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


# Тестирование на исключение.
@pytest.mark.parametrize("expected_exception, a, b", [(ZeroDivisionError, 10, 0),
                                                      (TypeError, 32, 're'),
                                                      (TypeError, "4343", 334)])
def test_division_with_error(expected_exception, a, b):
    with pytest.raises(expected_exception):
        division(a, b)
