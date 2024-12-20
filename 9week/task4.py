"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/recover-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.prev,self.changed,self.changed2=None,None,None
        def foo(x):
            if x.left: foo(x.left)
            if self.prev and x.val<self.prev.val:
                if not self.changed: self.changed=self.prev
                self.changed2=x
            self.prev=x
            if x.right: foo(x.right)
        if root: foo(root)
        self.changed.val, self.changed2.val = self.changed2.val, self.changed.val
        