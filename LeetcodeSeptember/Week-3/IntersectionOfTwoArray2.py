# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        if len(nums1) < len(nums2):
            shorter = sorted(nums1)
            longer = sorted(nums2)
        else:
            shorter = sorted(nums2)
            longer = sorted(nums1)

        i = j = 0
        out = []

        while i < len(shorter) and j < len(longer):
            if shorter[i] == longer[j]:
                out.append(shorter[i])
                i += 1
                j += 1
            elif shorter[i] < longer[j]:
                i += 1
            else:
                j += 1
        return out
