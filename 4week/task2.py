"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=array
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        m = nums[0]
        for i in range(1, len(nums)):
            s = max(nums[i], s + nums[i])
            if s > m:
                m = s
        return m