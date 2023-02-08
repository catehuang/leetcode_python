from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr: List[int], l: int, r: int) -> None:
            if l == r:
                return

            def merge(arr:List[int], l: int, m: int, r: int) -> None:
                # initial array with assigned size
                sortedArray = [0] * (r - l + 1)
                # sorted index
                k = 0
                # left's index
                i = l
                # right's index
                j = m + 1
                while i <= m and j <= r:
                    if arr[i] < arr[j]:
                        sortedArray[k] = arr[i]
                        i += 1
                    else:
                        sortedArray[k] = arr[j]
                        j += 1
                    k += 1
                # deal with remaining
                while i <= m:
                    sortedArray[k] = arr[i]
                    i += 1
                    k += 1
                while j <= r:
                    sortedArray[k] = arr[j]
                    j += 1
                    k += 1
                arr[l: l + len(sortedArray)] = sortedArray

            # get integer
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            return merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
