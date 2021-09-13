# https://leetcode.com/problems/maximum-number-of-balloons/
from typing import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = dict(Counter(text))
        x = 0
        while True:
            if hashMap.get('l', -1) >= 2 and hashMap.get('o', -1) >= 2 and hashMap.get('b', -1) >= 1 and hashMap.get('a', -1) >= 1 and hashMap.get('n', -1) >= 1:
                hashMap['l'] -= 2
                hashMap['o'] -= 2
                hashMap['b'] -= 1
                hashMap['a'] -= 1
                hashMap['n'] -= 1
                x += 1
            else:
                break
        return x


obj = Solution()
print(obj.maxNumberOfBalloons(text="loonbalxballpoon"))
