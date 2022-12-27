import pytest
from medium.longest_substring_without_repeating_characters import Solution


@pytest.fixture
def my_solution():
    solution = Solution()
    return solution


def test_length_of_longest_substring_case_1(my_solution):
    s = "abcabcbb"
    expected = 3
    assert my_solution.lengthOfLongestSubstring(s) == expected


def test_length_of_longest_substring_case_2(my_solution):
    s = "bbbbb"
    expected = 1
    assert my_solution.lengthOfLongestSubstring(s) == expected


def test_length_of_longest_substring_case_3(my_solution):
    s = "pwwkew"
    expected = 3
    assert my_solution.lengthOfLongestSubstring(s) == expected