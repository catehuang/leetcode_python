import math


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = []
        if len(s) < 2:
            return len(s)

        max_value = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] in myset:
                myset.remove(s[start])
                start += 1
            else:
                myset.append(s[end])
                end += 1
                max_value = max(len(myset), max_value)
        return max_value




