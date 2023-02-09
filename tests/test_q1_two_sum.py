import pytest
from easy.q1_two_sum import Solution


@pytest.fixture
def my_solution():
    solution = Solution()
    return solution


def test_two_sum_case_1(my_solution):
    assert my_solution.two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_case_2(my_solution):
    assert my_solution.two_sum([3, 2, 4], 6) == [1, 2]


def test_two_sum_case_3(my_solution):
    assert my_solution.two_sum([3, 3], 6) == [0, 1]

