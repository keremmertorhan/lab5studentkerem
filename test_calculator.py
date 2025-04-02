import pytest
import calculator

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (1, 1, 2),
    (5, 5, 10)
])
def test_add(a, b, expected):
    result = calculator.add(a, b)
    assert result == expected
