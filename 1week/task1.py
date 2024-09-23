"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = 0
        m = 1
        s1 = ''
        if s != "":
            if len(s) == 2 and s[0] != s[1]:
                return 2
            for i in range(len(s)):
                if s[i] not in s1:
                    s1 += s[i]
                    k += 1
                    m = max(k, m)
                else:
                    index = s1.index(s[i])
                    s1 = s1[index+1:] + s[i]
                    k = len(s1)
            return m
        else:
            return 0