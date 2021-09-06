from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        m = releaseTimes[0]
        has = [keysPressed[0]]
        for i in range(1, len(keysPressed)):
            temp = releaseTimes[i]-releaseTimes[i-1]
            if m < temp:
                m = temp
                has = [keysPressed[i]]
            elif m == temp:
                has.append(keysPressed[i])
        return sorted(has, reverse=True)[0]


x = [23, 34, 43, 59, 62, 80, 83, 92, 97]
y = "qgkzzihfc"
obj = Solution()
print(obj.slowestKey(x, y))
