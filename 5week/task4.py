"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=hash-table
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def backtrack(index: int, path: str):
            if index == len(digits):
                combinations.append(path)
                return
        
            poslet = map[digits[index]]
            for i in poslet:
                backtrack(index + 1, path + i)
        
        combinations = []
        backtrack(0,"")
        return combinations