import pytest
from main import multiplication


@pytest.mark.parametrize('a, b, c, result', [(10, 2, 3, 60),
                                             (100, 0.5, 5, 250)])
def test_multiplication_good(a, b, c, result):
    assert multiplication(a, b, c) == result