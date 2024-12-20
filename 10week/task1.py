"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=problem-list-v2&envId=binary-tree
"""
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = deque()
        queue.append(root)
        ans = []
        zigzag = False
        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if zigzag:
                level.reverse()          
            ans.append(level)
            zigzag = not zigzag
        return ans