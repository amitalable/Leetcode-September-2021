# https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s)-1
        m = list(range(65, 91))+list(range(97, 123))
        while i < j:
            if ord(s[i]) not in m:
                i += 1
                continue
            if ord(s[j]) not in m:
                j -= 1
                continue
            s = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
            i += 1
            j -= 1
        return s


obj = Solution()
res = obj.reverseOnlyLetters(s="a-bC-dEf-ghIj")
print(res)
