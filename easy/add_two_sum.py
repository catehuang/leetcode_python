from typing import Optional
from common.listnode import ListNode


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            if l1 is None:
                return l2
            else:
                return l1
        res = ListNode()
        tmp = res
        carry = 0
        while l1.next is not None or l2.next is not None:
            total = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            carry = int(total / 10)
            tmp.next = ListNode(total % 10)
            tmp = tmp.next
        if carry > 0:
            tmp.next = ListNode(carry)
        return res.next


