"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        res = []
        n = len(nums)
        consecutive = True
        consecutive_times = 0
        for i in range(1,k):
            if nums[i] == nums[i-1]+1:
                consecutive = True
                consecutive_times+=1
            else:
                consecutive = False
                consecutive_times = 0

        if consecutive and consecutive_times >= k-1:
            res.append(nums[k-1])
        else:
            res.append(-1)
        
        for i in range(k, n):
            if nums[i] == nums[i-1]+1:
                consecutive = True
                consecutive_times+=1
            else:
                consecutive = False
                consecutive_times = 0

            if consecutive and consecutive_times >= k-1:
                res.append(nums[i])
            else:
                res.append(-1)

        return res