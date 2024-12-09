"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                # We flip nums[i:i+3]
                nums[i], nums[i+1], nums[i+2] = 1-nums[i], 1-nums[i+1], 1-nums[i+2]
                flips += 1
        if nums[len(nums)-3:] == [1,1,1]:
            return flips
        return -1