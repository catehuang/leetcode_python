import pytest
from easy.q5_longest_palindromic_substring import Solution


@pytest.fixture
def my_solution():
    solution = Solution()
    return solution


def test_longest_palindrome_case_1(my_solution):
    result = my_solution.longestPalindrome("babad")
    expected1 = "bab"
    expected2 = "aba"
    assert result == expected1 or result == expected2


def test_longest_palindrome_case_2(my_solution):
    result = my_solution.longestPalindrome("cbbd")
    expected = "bb"
    assert result == expected


def test_longest_palindrome_case_3(my_solution):
    result = my_solution.longestPalindrome("")
    expected = ""
    assert result == expected


def test_longest_palindrome_case_4(my_solution):
    result = my_solution.longestPalindrome("aa5lpl5")
    expected = "5lpl5"
    assert result == expected
