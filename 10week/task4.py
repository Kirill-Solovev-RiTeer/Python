"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/?envType=problem-list-v2&envId=binary-tree
"""
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        dq.append(root)
        result = []
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            if level:
                result.append(level)
        return list(reversed(result))