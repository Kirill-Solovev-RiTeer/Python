"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/decode-string/submissions/1406504312/?envType=problem-list-v2&envId=string
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for i in s:
            if i == '[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ""
                curr_num = 0
            elif i == ']':
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            elif i.isdigit():
                curr_num = curr_num * 10 + int(i)
            else:
                curr_str += i
        return curr_str