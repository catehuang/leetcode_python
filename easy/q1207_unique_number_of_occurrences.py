from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # create key-value pair
        hashmap = {}
        for n in arr:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        values = []
        # check if the values are unique
        for key, value in hashmap.items():
            if value in values:
                return False
            else:
                values.append(value)
        return True
