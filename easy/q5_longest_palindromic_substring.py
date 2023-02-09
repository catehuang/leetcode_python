import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromMiddle(s: str, left: int, right: int) -> int:
            if s is None or left > right:
                return 0
            while left > 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if s is None or len(s) < 1:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # the length is odd
            len1 = expandFromMiddle(s, i, i)
            # the length is even
            len2 = expandFromMiddle(s, i, i + 1)
            length = max(len1, len2)

            if length > end - start:
                start = i - ((length - 1) // 2)
                end = i + length // 2

        return s[start: end + 1]
