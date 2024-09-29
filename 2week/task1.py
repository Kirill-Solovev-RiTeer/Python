"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=string
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
    
        for s in strs:
            key = ''.join(sorted(s))
            if key not in grouped:
                grouped[key] = [s]
            else:
                grouped[key].append(s)
        
        return list(grouped.values())