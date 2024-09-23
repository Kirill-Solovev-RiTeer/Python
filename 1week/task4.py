"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=string
"""
class Solution:
    from itertools import permutations
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        for x in permutations(s, r = len(s)):
            x = ''.join(x)
            arr.append(x)
        if t in arr:
            return True
        else:
            return False

        