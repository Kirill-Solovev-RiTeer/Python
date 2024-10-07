"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/next-permutation/description/?envType=problem-list-v2&envId=array
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums.sort()
            return nums
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        return nums
            

    