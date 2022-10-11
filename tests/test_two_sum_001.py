import pytest
from questions.two_sum_001 import Solution

@pytest.fixture
def my_sulution():
    return Solution();


def test_two_sum_case_1(my_sulution):
    assert my_sulution.two_Sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_case_2(my_sulution):
    assert my_sulution.two_Sum([3, 2, 4], 6) == [1, 2]


def test_two_sum_case_3(my_sulution):
    assert my_sulution.two_Sum([3, 3], 6) == [0, 1]
