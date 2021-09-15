# https://leetcode.com/problems/longest-turbulent-subarray
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        start = comp = max_length = end = 0
        n = len(arr)
        for end in range(1, n):
            if arr[end - 1] < arr[end]:
                if comp == -1:
                    max_length = max(max_length, end - start)
                    start = end - 1
                comp = -1
            elif arr[end - 1] > arr[end]:
                if comp == 1:
                    max_length = max(max_length, end - start)
                    start = end - 1
                comp = 1
            else:
                max_length = max(max_length, end - start)
                start = end
                comp = 0
        return max(max_length, end - start + 1)
