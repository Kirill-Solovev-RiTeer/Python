"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=array
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i,j = 0, len(height)-1
        
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            s = w*h
            max_area = max(max_area, s)

            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return max_area


        