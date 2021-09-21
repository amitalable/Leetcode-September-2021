# https://leetcode.com/problems/max-consecutive-ones/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # [1,1,0,1,1,1,0]
        # [1,0,1,1,0,1,0]
      
        i = 0
        j = i
        res = 0
        while j<len(nums):
            if nums[i] == 0:
                i+=1
            elif nums[j] == 0:
                res = max(res,j-i)
                i = j+1
            j +=1 
        return max(res,j-i)
