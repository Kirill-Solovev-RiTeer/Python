"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/description/?envType=problem-list-v2&envId=string
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = int(num1) * int(num2)
        return str(m)