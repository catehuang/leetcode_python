from typing import List
import pytest
from common.listnode import ListNode
from easy.add_two_sum import Solution


@pytest.fixture
def my_solution():
    solution = Solution()
    return solution


def create_list(array: List[int]):
    head = ListNode()
    current = head
    for val in array:
        current.next = ListNode(val)

    print(head.next)
    return head.next


def test_add_two_numbers_case_1(my_solution):
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = my_solution.add_two_numbers(l1, l2)
    expected = create_list([7, 0, 8])
    while expected is not None and expected.next is not None:
        assert result.val == expected.val
        result = result.next
        expected = expected.next


def test_add_two_numbers_case_2(my_solution):
    l1 = create_list([0])
    l2 = create_list([0])
    result = my_solution.add_two_numbers(l1, l2)
    expected = create_list([0])
    while expected is not None and expected.next is not None:
        assert result.val == expected.val
        result = result.next
        expected = expected.next


def test_add_two_numbers_case_3(my_solution):
    l1 = create_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_list([9, 9, 9, 9])
    result = my_solution.add_two_numbers(l1, l2)
    expected = create_list([8, 9, 9, 9, 0, 0, 0, 1])
    while expected is not None and expected.next is not None:
        assert result.val == expected.val
        result = result.next
        expected = expected.next
