"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=binary-tree
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:index] , postorder[0:index])
        root.right = self.buildTree(inorder[index + 1:] , postorder[index:-1]) 
        return root 