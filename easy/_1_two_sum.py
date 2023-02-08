# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
# to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = []
        for index in range(0, len(nums)):
            target_value = target - nums[index]
            if target_value in nums_hash:
                return [nums_hash.index(target_value), index]
            nums_hash.append(nums[index])
