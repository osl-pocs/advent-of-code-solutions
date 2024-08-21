import pytest
from day01.esloch import count_line

@pytest.mark.parametrize('path_file', ['2023/day01/tests/data_example.txt'])
def test_calculate_sum(path_file):
    result = count_line(path_file)

    assert result == 55971
