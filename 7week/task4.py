"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        maxSum = 0
        i, j = 0, 0
        max1, max2 = 0, 0
        while i < len(nums) - firstLen + 1:
            max1 = sum(nums[i:i + firstLen])
            if secondLen <= i:
                j = 0
                while j + secondLen <= i:
                    max2 = sum(nums[j:j + secondLen])
                    maxSum = max(maxSum, max1 + max2)
                    j += 1

            if len(nums) - (i + 1) >= secondLen:
                j = 0
                while j + i + secondLen <= len(nums):
                    max2 = sum(nums[i + j + firstLen:i + j + firstLen + secondLen])
                    maxSum = max(maxSum, max1 + max2)
                    j += 1
            i += 1
        return maxSum