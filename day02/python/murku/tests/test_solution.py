import pytest
# from solution import multiply_list

multiply_list_testdata = [
    ([1], 1),
    ([2, 3], 3),
    ([2, 5, 6], 60)
]

@pytest.mark.parametrize("numbers,expected", multiply_list_testdata)
def test_multiply_list(numbers, expected):
    actual = multiply_list(numbers)
    assert actual == expected, "test failed"
