"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=string
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        for i in range(len(s)):
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1: i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                continue 
            if i - max_len >= 0 and s[i - max_len: i + 1] == s[i - max_len: i + 1][::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]