# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
from typing import List
class Solution:
    def dfs(self, arr, pos, res):
        if len(res) != len(set(res)):
            return 0
        best = len(res)
        for i in range(pos,len(arr)):
            best = max(best,self.dfs(arr,i+1,res+arr[i]))
        return best
    
    def maxLength(self, arr: List[str]) -> int:
        return self.dfs(arr,0,"")
    