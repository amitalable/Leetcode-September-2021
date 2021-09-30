# https://leetcode.com/problems/partition-to-k-equal-sum-subsets
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(cur_sum, k):
            # terminal case
            if k == 0:
                return True
            if cur_sum == target:
                return backtrack(0, k-1)
            
            #backtrack
            for i in range(len(nums)):
                if not visited[i]:
                    if nums[i] > target:
                        return False
                    if cur_sum + nums[i] <= target:
                        visited[i] = True
                        if backtrack(cur_sum+nums[i], k):
                            return True
                        else:
                            visited[i] = False
            return False
            
        if sum(nums) % k: return False
        target = sum(nums) / k
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        return backtrack(0, k)