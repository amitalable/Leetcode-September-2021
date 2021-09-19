# https://leetcode.com/problems/distinct-subsequences
from collections import cache


class Solution:
    def numDistinct(self, s, t):
        @cache
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] == t[j]:
                return dp(i+1, j) + dp(i+1, j+1)
            return dp(i+1, j)

        return dp(0, 0)
