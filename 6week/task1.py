"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-window-substring/description/?envType=problem-list-v2&envId=sliding-window
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)

        min_len = float("inf")
        min_left, min_right = 0, 0

        while r < len(s):
            char = s[r]
            window_counts[char] += 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_left, min_right = l, r + 1
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                l += 1
            r += 1

        return "" if min_len == float("inf") else s[min_left:min_right]