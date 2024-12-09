"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        dic = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for ch in word2:
            dic[ch] += 1
        left = valid = count = 0
        size = len(word1)
        for i in range(size):
            ch = word1[i]
            if ch in dic:
                window[ch] += 1
                if window[ch] == dic[ch]:
                    valid += 1
            while valid == len(dic):
                count += size - i
                removed_ch = word1[left]
                left += 1
                if removed_ch in dic:
                    if window[removed_ch] == dic[removed_ch]:
                        valid -= 1
                    window[removed_ch] -= 1
        return count