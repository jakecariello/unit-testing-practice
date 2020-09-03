import pytest

@pytest.mark.parametrize('first_point, second_point, x, expected_y', [
    ((0, 0), (2, 3), 6, 9),
    ((1, 1), (5, 5), 7, 7),
    ((0, 2), (2, 0), 1, 1)
])
def test_on_line(first_point, second_point, x, expected_y):
    from on_line import on_line
    assert on_line(first_point, second_point, x) == expected_y
