"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=problem-list-v2&envId=string
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join(reversed(s.split()))
        return s

# Пример использования
s = "a good   example"
solution = Solution()
print(solution.reverseWords(s))