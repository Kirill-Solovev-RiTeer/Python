"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=array
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = merged[-1]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)