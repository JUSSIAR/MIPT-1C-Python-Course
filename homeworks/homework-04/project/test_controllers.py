import pytest
from controllers import operation

@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (5, -4, 1), (7, 8, 15)])
def test_operation(a, b, expected):
    received = operation(a, b)
    assert received == expected
