"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        count = 0
        curr = 0
        for i in range(2 , len(nums)):
            if nums[i-1] - nums[i] == nums[i-2] - nums[i-1]:
                curr += 1
                count += curr
            else:
                curr = 0
        return count