# https://leetcode.com/problems/unique-binary-search-trees-ii
from itertools import product


class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        def dp(i, j):
            if i > j:
                return [None]
            ans = []

            for k in range(i, j + 1):
                for lft, rgh in product(dp(i, k-1), dp(k+1, j)):
                    root = ListNode(k)
                    root.left = lft
                    root.right = rgh
                    ans.append(root)
            return ans

        return dp(1, n)
