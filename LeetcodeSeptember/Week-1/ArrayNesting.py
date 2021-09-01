# https://leetcode.com/problems/array-nesting
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        i = 0
        max_count = 0
        check = [False] * (len(nums))
        while i < len(nums):
            if check[i] == False:
                temp_set = set()
                while i not in temp_set:
                    temp_set.add(i)
                    check[i] = True
                    i = nums[i]
                max_count = max(max_count, len(temp_set))
            i += 1
        return max_count
