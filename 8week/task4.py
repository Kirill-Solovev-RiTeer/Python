"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans, n = 0, len(s)
        idxs = [i for i, c in enumerate(s) if c == '0']
        idxs.append(n)
        for i in range(n):
            pos = bisect_left(idxs, i)
            if s[i] == '1': ans += idxs[pos] - i
            pos += 1
            cnt = 1
            while pos < len(idxs) and i + cnt + cnt ** 2 <= n:
                if idxs[pos] - i + 1 - cnt > cnt ** 2:
                    ans += min(idxs[pos] - idxs[pos - 1], idxs[pos] - i + 1 - cnt - cnt ** 2)
                cnt += 1
                pos += 1
        return ans