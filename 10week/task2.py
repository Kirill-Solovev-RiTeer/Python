"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=problem-list-v2&envId=binary-tree
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        hashmap = {}
        for i, val in enumerate(inorder):
            hashmap[val] = i
        
        def helper(left, right):
            if left > right:
                return None
            
            root = TreeNode(preorder.popleft())
            mid = hashmap[root.val]

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root
        
        return helper(0, len(inorder)-1)