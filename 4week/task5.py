"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/rotate-array/description/?envType=problem-list-v2&envId=array
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
