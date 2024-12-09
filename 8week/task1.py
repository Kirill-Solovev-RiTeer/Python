"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        i = j = 0
        hashMap = defaultdict(int)
        count = int((n * (n + 1)) / 2)

        while j < n:
            hashMap[s[j]] += 1
            while i <= j and hashMap[s[j]] == k:
                hashMap[s[i]] -= 1
                i += 1
            count -= (j - i + 1)
            j += 1

        return count