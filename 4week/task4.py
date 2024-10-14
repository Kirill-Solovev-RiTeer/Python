"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=array
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        m = 0
        for i in num:
            if i - 1 not in num:
                curr = i
                k = 1
                while curr + 1 in num:
                    curr += 1
                    k += 1
                m = max(m,k)
        return m