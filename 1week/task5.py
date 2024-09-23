"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/maximum-product-of-word-lengths/?envType=problem-list-v2&envId=string
"""
class Solution(object):
    def maxProduct(self, words):
        max_len = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(set(words[i]) & set(words[j])) == 0:
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        return max_len
        