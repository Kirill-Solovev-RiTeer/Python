"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/description/?envType=problem-list-v2&envId=string
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            else:
                break

        num *= sign

        num = max(-2**31, min(num, 2**31-1))
        
        return num