"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = left = right = 0
        if k <= 1:
            return count
        p = 1

        while right < len(nums):
            p *= nums[right]
            while p >= k:
                p //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1
        
        return count