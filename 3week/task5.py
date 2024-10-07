"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/permutations-ii/description/?envType=problem-list-v2&envId=array
"""
class Solution:
    from itertools import permutations
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for x in set(permutations(nums)):
            arr.append(x)
        return arr